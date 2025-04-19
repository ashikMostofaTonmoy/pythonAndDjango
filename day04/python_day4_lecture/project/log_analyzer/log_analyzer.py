#!/usr/bin/env python3
"""
Log File Analyzer

A command-line application that analyzes log files using regular expressions.
Features:
- Parse log files using regular expressions
- Extract important information (timestamps, IP addresses, error codes, etc.)
- Generate statistics and reports
- Filter logs based on various criteria
- Detect patterns or anomalies in the logs

This project demonstrates the use of:
- Regular expressions (regex)
- File I/O operations
- Exception handling
- String manipulation
- Data analysis and reporting
"""

import re
import os
import sys
import datetime
import json
import argparse
from typing import List, Dict, Any, Optional, Tuple
from collections import Counter, defaultdict


class LogEntry:
    """Class representing a single log entry with parsed components."""
    
    def __init__(self, raw_log: str, timestamp: datetime.datetime, ip_address: str, 
                 method: str, path: str, status_code: int, response_size: int,
                 user_agent: Optional[str] = None, referer: Optional[str] = None):
        """
        Initialize a LogEntry object.
        
        Args:
            raw_log: The original log line
            timestamp: The timestamp of the log entry
            ip_address: The IP address of the client
            method: The HTTP method (GET, POST, etc.)
            path: The requested path
            status_code: The HTTP status code
            response_size: The size of the response in bytes
            user_agent: The user agent string (default: None)
            referer: The referer URL (default: None)
        """
        self.raw_log = raw_log
        self.timestamp = timestamp
        self.ip_address = ip_address
        self.method = method
        self.path = path
        self.status_code = status_code
        self.response_size = response_size
        self.user_agent = user_agent
        self.referer = referer
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the LogEntry object to a dictionary.
        
        Returns:
            A dictionary representation of the LogEntry
        """
        return {
            'timestamp': self.timestamp.isoformat(),
            'ip_address': self.ip_address,
            'method': self.method,
            'path': self.path,
            'status_code': self.status_code,
            'response_size': self.response_size,
            'user_agent': self.user_agent,
            'referer': self.referer
        }
    
    def __str__(self) -> str:
        """
        Return a string representation of the LogEntry.
        
        Returns:
            A formatted string with log entry details
        """
        return (f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.ip_address} - "
                f"{self.method} {self.path} - {self.status_code} - {self.response_size} bytes")


class LogParser:
    """Class for parsing log files using regular expressions."""
    
    # Common log format pattern (Apache/Nginx)
    # Example: 192.168.1.1 - - [19/Apr/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
    COMMON_LOG_PATTERN = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "([A-Z]+) (.*?) HTTP/\d\.\d" (\d+) (\d+)'
    )
    
    # Combined log format pattern (Apache/Nginx with user agent and referer)
    # Example: 192.168.1.1 - - [19/Apr/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326 "http://example.com" "Mozilla/5.0 ..."
    COMBINED_LOG_PATTERN = re.compile(
        r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "([A-Z]+) (.*?) HTTP/\d\.\d" (\d+) (\d+) "(.*?)" "(.*?)"'
    )
    
    # Custom log format patterns can be added here
    
    @staticmethod
    def parse_timestamp(timestamp_str: str) -> datetime.datetime:
        """
        Parse a timestamp string from a log file.
        
        Args:
            timestamp_str: The timestamp string (e.g., "19/Apr/2023:13:55:36 +0000")
            
        Returns:
            A datetime object
            
        Raises:
            ValueError: If the timestamp format is invalid
        """
        try:
            # Remove timezone information for simplicity
            timestamp_str = timestamp_str.split(' ')[0]
            return datetime.datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid timestamp format: {timestamp_str}")
    
    @classmethod
    def parse_log_line(cls, log_line: str) -> Optional[LogEntry]:
        """
        Parse a single log line.
        
        Args:
            log_line: A single line from a log file
            
        Returns:
            A LogEntry object if parsing succeeds, None otherwise
        """
        # Try combined log format first
        match = cls.COMBINED_LOG_PATTERN.match(log_line)
        if match:
            ip_address, timestamp_str, method, path, status_code, response_size, referer, user_agent = match.groups()
            
            try:
                timestamp = cls.parse_timestamp(timestamp_str)
                return LogEntry(
                    raw_log=log_line,
                    timestamp=timestamp,
                    ip_address=ip_address,
                    method=method,
                    path=path,
                    status_code=int(status_code),
                    response_size=int(response_size),
                    referer=referer if referer != "-" else None,
                    user_agent=user_agent if user_agent != "-" else None
                )
            except ValueError as e:
                print(f"Error parsing log line: {e}")
                return None
        
        # Try common log format
        match = cls.COMMON_LOG_PATTERN.match(log_line)
        if match:
            ip_address, timestamp_str, method, path, status_code, response_size = match.groups()
            
            try:
                timestamp = cls.parse_timestamp(timestamp_str)
                return LogEntry(
                    raw_log=log_line,
                    timestamp=timestamp,
                    ip_address=ip_address,
                    method=method,
                    path=path,
                    status_code=int(status_code),
                    response_size=int(response_size)
                )
            except ValueError as e:
                print(f"Error parsing log line: {e}")
                return None
        
        # No match found
        return None
    
    @classmethod
    def parse_log_file(cls, filename: str) -> List[LogEntry]:
        """
        Parse a log file and return a list of LogEntry objects.
        
        Args:
            filename: The path to the log file
            
        Returns:
            A list of LogEntry objects
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            IOError: If there's an error reading the file
        """
        log_entries = []
        
        try:
            with open(filename, 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if not line:
                        continue
                    
                    log_entry = cls.parse_log_line(line)
                    if log_entry:
                        log_entries.append(log_entry)
                    else:
                        print(f"Warning: Could not parse line {line_num}: {line[:50]}...")
        except (FileNotFoundError, IOError) as e:
            print(f"Error reading log file: {e}")
            raise
        
        return log_entries


class LogAnalyzer:
    """Class for analyzing log entries and generating reports."""
    
    def __init__(self, log_entries: List[LogEntry]):
        """
        Initialize a LogAnalyzer object.
        
        Args:
            log_entries: A list of LogEntry objects to analyze
        """
        self.log_entries = log_entries
    
    def filter_by_date_range(self, start_date: datetime.datetime, 
                            end_date: datetime.datetime) -> List[LogEntry]:
        """
        Filter log entries by date range.
        
        Args:
            start_date: The start date of the range
            end_date: The end date of the range
            
        Returns:
            A list of LogEntry objects within the specified date range
        """
        return [
            entry for entry in self.log_entries 
            if start_date <= entry.timestamp <= end_date
        ]
    
    def filter_by_ip(self, ip_address: str) -> List[LogEntry]:
        """
        Filter log entries by IP address.
        
        Args:
            ip_address: The IP address to filter by
            
        Returns:
            A list of LogEntry objects with the specified IP address
        """
        return [
            entry for entry in self.log_entries 
            if entry.ip_address == ip_address
        ]
    
    def filter_by_method(self, method: str) -> List[LogEntry]:
        """
        Filter log entries by HTTP method.
        
        Args:
            method: The HTTP method to filter by (GET, POST, etc.)
            
        Returns:
            A list of LogEntry objects with the specified HTTP method
        """
        return [
            entry for entry in self.log_entries 
            if entry.method == method.upper()
        ]
    
    def filter_by_status_code(self, status_code: int) -> List[LogEntry]:
        """
        Filter log entries by HTTP status code.
        
        Args:
            status_code: The HTTP status code to filter by
            
        Returns:
            A list of LogEntry objects with the specified status code
        """
        return [
            entry for entry in self.log_entries 
            if entry.status_code == status_code
        ]
    
    def filter_by_status_code_range(self, start_code: int, end_code: int) -> List[LogEntry]:
        """
        Filter log entries by HTTP status code range.
        
        Args:
            start_code: The start of the status code range
            end_code: The end of the status code range
            
        Returns:
            A list of LogEntry objects with status codes in the specified range
        """
        return [
            entry for entry in self.log_entries 
            if start_code <= entry.status_code <= end_code
        ]
    
    def filter_by_path_pattern(self, pattern: str) -> List[LogEntry]:
        """
        Filter log entries by path pattern.
        
        Args:
            pattern: A regex pattern to match against the path
            
        Returns:
            A list of LogEntry objects with paths matching the pattern
        """
        regex = re.compile(pattern)
        return [
            entry for entry in self.log_entries 
            if regex.search(entry.path)
        ]
    
    def get_top_ips(self, limit: int = 10) -> List[Tuple[str, int]]:
        """
        Get the top IP addresses by request count.
        
        Args:
            limit: The maximum number of results to return
            
        Returns:
            A list of tuples (ip_address, count) sorted by count in descending order
        """
        ip_counter = Counter(entry.ip_address for entry in self.log_entries)
        return ip_counter.most_common(limit)
    
    def get_top_paths(self, limit: int = 10) -> List[Tuple[str, int]]:
        """
        Get the top requested paths by request count.
        
        Args:
            limit: The maximum number of results to return
            
        Returns:
            A list of tuples (path, count) sorted by count in descending order
        """
        path_counter = Counter(entry.path for entry in self.log_entries)
        return path_counter.most_common(limit)
    
    def get_status_code_distribution(self) -> Dict[int, int]:
        """
        Get the distribution of HTTP status codes.
        
        Returns:
            A dictionary mapping status codes to their counts
        """
        return dict(Counter(entry.status_code for entry in self.log_entries))
    
    def get_method_distribution(self) -> Dict[str, int]:
        """
        Get the distribution of HTTP methods.
        
        Returns:
            A dictionary mapping HTTP methods to their counts
        """
        return dict(Counter(entry.method for entry in self.log_entries))
    
    def get_hourly_distribution(self) -> Dict[int, int]:
        """
        Get the distribution of requests by hour of day.
        
        Returns:
            A dictionary mapping hours (0-23) to request counts
        """
        hour_counter = Counter(entry.timestamp.hour for entry in self.log_entries)
        return {hour: hour_counter.get(hour, 0) for hour in range(24)}
    
    def get_daily_distribution(self) -> Dict[str, int]:
        """
        Get the distribution of requests by day.
        
        Returns:
            A dictionary mapping dates (as strings) to request counts
        """
        day_counter = Counter(entry.timestamp.date().isoformat() for entry in self.log_entries)
        return dict(day_counter)
    
    def get_total_bandwidth(self) -> int:
        """
        Calculate the total bandwidth used (sum of response sizes).
        
        Returns:
            The total bandwidth in bytes
        """
        return sum(entry.response_size for entry in self.log_entries)
    
    def get_average_response_size(self) -> float:
        """
        Calculate the average response size.
        
        Returns:
            The average response size in bytes
        """
        if not self.log_entries:
            return 0
        return self.get_total_bandwidth() / len(self.log_entries)
    
    def detect_potential_attacks(self) -> Dict[str, List[LogEntry]]:
        """
        Detect potential attacks or suspicious activity.
        
        Returns:
            A dictionary mapping attack types to lists of suspicious log entries
        """
        suspicious_entries = defaultdict(list)
        
        # SQL injection attempts
        sql_injection_pattern = re.compile(r'(\'|\"|\s+or\s+|\s+and\s+|\s+union\s+|select\s+|drop\s+|--)', re.IGNORECASE)
        for entry in self.log_entries:
            if sql_injection_pattern.search(entry.path):
                suspicious_entries['sql_injection'].append(entry)
        
        # Path traversal attempts
        path_traversal_pattern = re.compile(r'(\.\./|\.\.\\)')
        for entry in self.log_entries:
            if path_traversal_pattern.search(entry.path):
                suspicious_entries['path_traversal'].append(entry)
        
        # Excessive 404 errors from same IP
        ip_404_counts = defaultdict(int)
        for entry in self.log_entries:
            if entry.status_code == 404:
                ip_404_counts[entry.ip_address] += 1
        
        for ip, count in ip_404_counts.items():
            if count > 10:  # Threshold for suspicious activity
                suspicious_entries['excessive_404s'].extend(
                    entry for entry in self.log_entries 
                    if entry.ip_address == ip and entry.status_code == 404
                )
        
        return suspicious_entries
    
    def generate_summary_report(self) -> Dict[str, Any]:
        """
        Generate a summary report of the log analysis.
        
        Returns:
            A dictionary containing various statistics and insights
        """
        if not self.log_entries:
            return {"error": "No log entries to analyze"}
        
        # Get date range
        start_date = min(entry.timestamp for entry in self.log_entries)
        end_date = max(entry.timestamp for entry in self.log_entries)
        
        # Calculate time span
        time_span = end_date - start_date
        
        return {
            "total_requests": len(self.log_entries),
            "date_range": {
                "start": start_date.isoformat(),
                "end": end_date.isoformat(),
                "span_days": time_span.days + (time_span.seconds / 86400)
            },
            "top_ips": self.get_top_ips(5),
            "top_paths": self.get_top_paths(5),
            "status_codes": self.get_status_code_distribution(),
            "methods": self.get_method_distribution(),
            "total_bandwidth": self.get_total_bandwidth(),
            "average_response_size": self.get_average_response_size(),
            "potential_attacks": {
                attack_type: len(entries) 
                for attack_type, entries in self.detect_potential_attacks().items()
            }
        }


class LogAnalyzerCLI:
    """Command-line interface for the Log File Analyzer application."""
    
    def __init__(self):
        """Initialize the CLI."""
        self.log_entries = []
        self.analyzer = None
    
    def parse_args(self) -> argparse.Namespace:
        """
        Parse command-line arguments.
        
        Returns:
            An argparse.Namespace object containing the parsed arguments
        """
        parser = argparse.ArgumentParser(description="Analyze log files using regular expressions")
        
        parser.add_argument("log_file", help="Path to the log file to analyze")
        
        parser.add_argument("--output", "-o", help="Output file for the report (JSON format)")
        
        parser.add_argument("--filter-ip", help="Filter by IP address")
        parser.add_argument("--filter-method", help="Filter by HTTP method")
        parser.add_argument("--filter-status", type=int, help="Filter by HTTP status code")
        parser.add_argument("--filter-path", help="Filter by path pattern (regex)")
        
        parser.add_argument("--start-date", help="Start date for filtering (YYYY-MM-DD)")
        parser.add_argument("--end-date", help="End date for filtering (YYYY-MM-DD)")
        
        parser.add_argument("--top-ips", type=int, default=10, help="Number of top IPs to show")
        parser.add_argument("--top-paths", type=int, default=10, help="Number of top paths to show")
        
        parser.add_argument("--show-attacks", action="store_true", help="Show potential attacks")
        parser.add_argument("--show-hourly", action="store_true", help="Show hourly distribution")
        parser.add_argument("--show-daily", action="store_true", help="Show daily distribution")
        
        return parser.parse_args()
    
    def load_log_file(self, filename: str) -> None:
        """
        Load and parse a log file.
        
        Args:
            filename: The path to the log file
        """
        try:
            print(f"Loading log file: {filename}")
            self.log_entries = LogParser.parse_log_file(filename)
            print(f"Loaded {len(self.log_entries)} log entries")
            self.analyzer = LogAnalyzer(self.log_entries)
        except Exception as e:
            print(f"Error loading log file: {e}")
            sys.exit(1)
    
    def apply_filters(self, args: argparse.Namespace) -> None:
        """
        Apply filters based on command-line arguments.
        
        Args:
            args: The parsed command-line arguments
        """
        filtered_entries = self.log_entries
        
        if args.filter_ip:
            filtered_entries = [entry for entry in filtered_entries if entry.ip_address == args.filter_ip]
            print(f"Filtered by IP: {args.filter_ip} ({len(filtered_entries)} entries)")
        
        if args.filter_method:
            filtered_entries = [entry for entry in filtered_entries if entry.method == args.filter_method.upper()]
            print(f"Filtered by method: {args.filter_method} ({len(filtered_entries)} entries)")
        
        if args.filter_status:
            filtered_entries = [entry for entry in filtered_entries if entry.status_code == args.filter_status]
            print(f"Filtered by status code: {args.filter_status} ({len(filtered_entries)} entries)")
        
        if args.filter_path:
            try:
                regex = re.compile(args.filter_path)
                filtered_entries = [entry for entry in filtered_entries if regex.search(entry.path)]
                print(f"Filtered by path pattern: {args.filter_path} ({len(filtered_entries)} entries)")
            except re.error as e:
                print(f"Invalid regex pattern: {e}")
        
        if args.start_date:
            try:
                start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
                filtered_entries = [entry for entry in filtered_entries if entry.timestamp >= start_date]
                print(f"Filtered by start date: {args.start_date} ({len(filtered_entries)} entries)")
            except ValueError:
                print(f"Invalid start date format: {args.start_date}")
        
        if args.end_date:
            try:
                end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d")
                end_date = end_date + datetime.timedelta(days=1)  # Include the end date
                filtered_entries = [entry for entry in filtered_entries if entry.timestamp <= end_date]
                print(f"Filtered by end date: {args.end_date} ({len(filtered_entries)} entries)")
            except ValueError:
                print(f"Invalid end date format: {args.end_date}")
        
        self.analyzer = LogAnalyzer(filtered_entries)
    
    def display_summary(self) -> None:
        """Display a summary of the log analysis."""
        if not self.analyzer:
            print("No log entries to analyze")
            return
        
        summary = self.analyzer.generate_summary_report()
        
        print("\n===== Log Analysis Summary =====")
        print(f"Total Requests: {summary['total_requests']}")
        
        start_date = datetime.datetime.fromisoformat(summary['date_range']['start'])
        end_date = datetime.datetime.fromisoformat(summary['date_range']['end'])
        print(f"Date Range: {start_date.strftime('%Y-%m-%d %H:%M:%S')} to {end_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Time Span: {summary['date_range']['span_days']:.2f} days")
        
        print("\nHTTP Methods:")
        for method, count in summary['methods'].items():
            print(f"  {method}: {count}")
        
        print("\nStatus Codes:")
        for status, count in summary['status_codes'].items():
            print(f"  {status}: {count}")
        
        print(f"\nTotal Bandwidth: {summary['total_bandwidth'] / 1024 / 1024:.2f} MB")
        print(f"Average Response Size: {summary['average_response_size'] / 1024:.2f} KB")
        
        if summary['potential_attacks']:
            print("\nPotential Attacks Detected:")
            for attack_type, count in summary['potential_attacks'].items():
                print(f"  {attack_type}: {count}")
        
        print("===============================")
    
    def display_top_ips(self, limit: int) -> None:
        """
        Display the top IP addresses by request count.
        
        Args:
            limit: The maximum number of results to display
        """
        if not self.analyzer:
            return
        
        top_ips = self.analyzer.get_top_ips(limit)
        
        print(f"\n===== Top {len(top_ips)} IP Addresses =====")
        for ip, count in top_ips:
            print(f"{ip}: {count} requests")
    
    def display_top_paths(self, limit: int) -> None:
        """
        Display the top requested paths by request count.
        
        Args:
            limit: The maximum number of results to display
        """
        if not self.analyzer:
            return
        
        top_paths = self.analyzer.get_top_paths(limit)
        
        print(f"\n===== Top {len(top_paths)} Requested Paths =====")
        for path, count in top_paths:
            print(f"{path}: {count} requests")
    
    def display_hourly_distribution(self) -> None:
        """Display the distribution of requests by hour of day."""
        if not self.analyzer:
            return
        
        hourly_dist = self.analyzer.get_hourly_distribution()
        
        print("\n===== Hourly Request Distribution =====")
        max_count = max(hourly_dist.values()) if hourly_dist else 0
        
        for hour in range(24):
            count = hourly_dist.get(hour, 0)
            bar_length = int((count / max_count) * 50) if max_count > 0 else 0
            print(f"{hour:02d}:00 - {hour:02d}:59: {count:5d} {'#' * bar_length}")
    
    def display_daily_distribution(self) -> None:
        """Display the distribution of requests by day."""
        if not self.analyzer:
            return
        
        daily_dist = self.analyzer.get_daily_distribution()
        
        print("\n===== Daily Request Distribution =====")
        for date_str, count in sorted(daily_dist.items()):
            print(f"{date_str}: {count} requests")
    
    def display_potential_attacks(self) -> None:
        """Display potential attacks or suspicious activity."""
        if not self.analyzer:
            return
        
        attacks = self.analyzer.detect_potential_attacks()
        
        if not attacks:
            print("\nNo potential attacks detected.")
            return
        
        print("\n===== Potential Attacks =====")
        for attack_type, entries in attacks.items():
            print(f"\n{attack_type.replace('_', ' ').title()} ({len(entries)} instances):")
            for i, entry in enumerate(entries[:5], 1):  # Show only first 5 instances
                print(f"  {i}. {entry}")
            
            if len(entries) > 5:
                print(f"  ... and {len(entries) - 5} more")
    
    def save_report(self, filename: str) -> None:
        """
        Save the analysis report to a JSON file.
        
        Args:
            filename: The path to the output file
        """
        if not self.analyzer:
            print("No log entries to analyze")
            return
        
        try:
            summary = self.analyzer.generate_summary_report()
            
            # Add additional data
            summary['top_ips_full'] = self.analyzer.get_top_ips(20)
            summary['top_paths_full'] = self.analyzer.get_top_paths(20)
            summary['hourly_distribution'] = self.analyzer.get_hourly_distribution()
            summary['daily_distribution'] = self.analyzer.get_daily_distribution()
            
            # Convert potential attacks to a more JSON-friendly format
            attacks = self.analyzer.detect_potential_attacks()
            summary['potential_attacks_details'] = {
                attack_type: [entry.to_dict() for entry in entries[:10]]  # Limit to 10 examples
                for attack_type, entries in attacks.items()
            }
            
            with open(filename, 'w') as f:
                json.dump(summary, f, indent=4)
            
            print(f"\nReport saved to {filename}")
        except Exception as e:
            print(f"Error saving report: {e}")
    
    def run(self) -> None:
        """Run the CLI application."""
        args = self.parse_args()
        
        self.load_log_file(args.log_file)
        self.apply_filters(args)
        
        self.display_summary()
        self.display_top_ips(args.top_ips)
        self.display_top_paths(args.top_paths)
        
        if args.show_hourly:
            self.display_hourly_distribution()
        
        if args.show_daily:
            self.display_daily_distribution()
        
        if args.show_attacks:
            self.display_potential_attacks()
        
        if args.output:
            self.save_report(args.output)


def generate_sample_log() -> None:
    """Generate a sample log file for testing."""
    sample_log_path = "sample_log.txt"
    
    # Sample IP addresses
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "10.0.0.1", "10.0.0.2"]
    
    # Sample paths
    paths = [
        "/index.html", 
        "/about.html", 
        "/contact.html", 
        "/products/item1.html", 
        "/products/item2.html",
        "/admin/login.php",
        "/images/logo.png",
        "/css/style.css",
        "/js/script.js",
        "/api/data"
    ]
    
    # Sample methods
    methods = ["GET", "POST", "PUT", "DELETE"]
    
    # Sample status codes
    status_codes = [200, 201, 301, 302, 400, 401, 403, 404, 500, 503]
    
    # Sample user agents
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    ]
    
    # Generate log entries
    import random
    
    log_entries = []
    
    # Generate normal log entries
    start_date = datetime.datetime(2023, 4, 1)
    end_date = datetime.datetime(2023, 4, 30)
    delta = end_date - start_date
    
    for _ in range(1000):
        # Random date within range
        random_seconds = random.randint(0, delta.total_seconds())
        log_date = start_date + datetime.timedelta(seconds=random_seconds)
        date_str = log_date.strftime("%d/%b/%Y:%H:%M:%S")
        
        ip = random.choice(ips)
        method = random.choice(methods)
        path = random.choice(paths)
        status = random.choice(status_codes)
        size = random.randint(100, 10000)
        user_agent = random.choice(user_agents)
        
        log_entry = f'{ip} - - [{date_str} +0000] "{method} {path} HTTP/1.1" {status} {size} "-" "{user_agent}"'
        log_entries.append(log_entry)
    
    # Add some suspicious entries
    
    # SQL injection attempts
    sql_injection_paths = [
        "/search?q=1' OR '1'='1",
        "/login?username=admin'--&password=anything",
        "/products?id=1 UNION SELECT username,password FROM users",
        "/profile?id=1; DROP TABLE users",
        "/api/data?filter=name='admin' OR 1=1"
    ]
    
    for _ in range(20):
        log_date = start_date + datetime.timedelta(seconds=random.randint(0, delta.total_seconds()))
        date_str = log_date.strftime("%d/%b/%Y:%H:%M:%S")
        
        ip = "192.168.1.100"  # Suspicious IP
        method = "GET"
        path = random.choice(sql_injection_paths)
        status = 400  # Bad request
        size = random.randint(100, 500)
        user_agent = random.choice(user_agents)
        
        log_entry = f'{ip} - - [{date_str} +0000] "{method} {path} HTTP/1.1" {status} {size} "-" "{user_agent}"'
        log_entries.append(log_entry)
    
    # Path traversal attempts
    path_traversal_paths = [
        "/../../etc/passwd",
        "/../../../etc/shadow",
        "/images/../../config.php",
        "/download?file=../../../etc/passwd",
        "/theme/../../config/database.php"
    ]
    
    for _ in range(15):
        log_date = start_date + datetime.timedelta(seconds=random.randint(0, delta.total_seconds()))
        date_str = log_date.strftime("%d/%b/%Y:%H:%M:%S")
        
        ip = "10.0.0.100"  # Another suspicious IP
        method = "GET"
        path = random.choice(path_traversal_paths)
        status = 404  # Not found
        size = random.randint(100, 500)
        user_agent = random.choice(user_agents)
        
        log_entry = f'{ip} - - [{date_str} +0000] "{method} {path} HTTP/1.1" {status} {size} "-" "{user_agent}"'
        log_entries.append(log_entry)
    
    # Excessive 404 errors
    for _ in range(30):
        log_date = start_date + datetime.timedelta(seconds=random.randint(0, delta.total_seconds()))
        date_str = log_date.strftime("%d/%b/%Y:%H:%M:%S")
        
        ip = "192.168.1.200"  # IP with many 404s
        method = "GET"
        path = f"/not-found-{random.randint(1, 100)}.html"
        status = 404  # Not found
        size = random.randint(100, 500)
        user_agent = random.choice(user_agents)
        
        log_entry = f'{ip} - - [{date_str} +0000] "{method} {path} HTTP/1.1" {status} {size} "-" "{user_agent}"'
        log_entries.append(log_entry)
    
    # Shuffle and write to file
    random.shuffle(log_entries)
    
    with open(sample_log_path, 'w') as f:
        for entry in log_entries:
            f.write(entry + '\n')
    
    print(f"Sample log file generated: {sample_log_path}")
    print(f"Contains {len(log_entries)} log entries")


def main():
    """Main function to run the Log File Analyzer application."""
    # Check if we need to generate a sample log file
    if len(sys.argv) > 1 and sys.argv[1] == "--generate-sample":
        generate_sample_log()
        return
    
    # Run the CLI
    cli = LogAnalyzerCLI()
    cli.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")
        sys.exit(0)
