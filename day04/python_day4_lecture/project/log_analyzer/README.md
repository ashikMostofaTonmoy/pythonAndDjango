# Log File Analyzer

A command-line application that analyzes log files using regular expressions, demonstrating the practical application of regex, string manipulation, and data analysis in Python.

## Features

- Parse log files using regular expressions
- Extract important information (timestamps, IP addresses, HTTP methods, paths, status codes, etc.)
- Generate statistics and reports
- Filter logs based on various criteria:
  - IP address
  - HTTP method
  - Status code
  - Path pattern
  - Date range
- Detect patterns or anomalies in the logs:
  - SQL injection attempts
  - Path traversal attempts
  - Excessive 404 errors
- Generate and save comprehensive reports in JSON format
- Visualize request distributions by hour and day

## Concepts Demonstrated

This project demonstrates several key Python concepts covered in the Day 4 lecture:

1. **Regular Expressions (Regex)**
   - Pattern matching with complex patterns
   - Extracting information using capture groups
   - Validating and filtering text data

2. **String Manipulation**
   - Parsing and formatting strings
   - Converting between different string formats
   - String validation and cleaning

3. **Exception Handling**
   - Using try/except blocks to handle errors
   - Handling specific exceptions (FileNotFoundError, ValueError, etc.)
   - Graceful error recovery

4. **Date and Time Handling**
   - Parsing timestamps from strings
   - Date arithmetic and comparisons
   - Formatting dates for display

5. **JSON Data Processing**
   - Converting Python objects to JSON
   - Structuring data for serialization
   - Saving analysis results to JSON files

6. **Command-Line Interface**
   - Parsing command-line arguments
   - Providing a user-friendly interface
   - Generating formatted output

## Project Structure

The project consists of four main classes:

1. **LogEntry**: Represents a single log entry with parsed components.
2. **LogParser**: Parses log files using regular expressions.
3. **LogAnalyzer**: Analyzes log entries and generates reports.
4. **LogAnalyzerCLI**: Provides a command-line interface for the application.

## How to Run

1. Make sure you have Python 3.6 or higher installed
2. Navigate to the project directory
3. Run the script with a log file:
   ```
   python log_analyzer.py access.log
   ```

4. Generate a sample log file for testing:
   ```
   python log_analyzer.py --generate-sample
   ```

## Command-Line Options

```
usage: log_analyzer.py [-h] [--output OUTPUT] [--filter-ip FILTER_IP]
                       [--filter-method FILTER_METHOD] [--filter-status FILTER_STATUS]
                       [--filter-path FILTER_PATH] [--start-date START_DATE]
                       [--end-date END_DATE] [--top-ips TOP_IPS] [--top-paths TOP_PATHS]
                       [--show-attacks] [--show-hourly] [--show-daily]
                       log_file

Analyze log files using regular expressions

positional arguments:
  log_file              Path to the log file to analyze

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file for the report (JSON format)
  --filter-ip FILTER_IP
                        Filter by IP address
  --filter-method FILTER_METHOD
                        Filter by HTTP method
  --filter-status FILTER_STATUS
                        Filter by HTTP status code
  --filter-path FILTER_PATH
                        Filter by path pattern (regex)
  --start-date START_DATE
                        Start date for filtering (YYYY-MM-DD)
  --end-date END_DATE   End date for filtering (YYYY-MM-DD)
  --top-ips TOP_IPS     Number of top IPs to show
  --top-paths TOP_PATHS
                        Number of top paths to show
  --show-attacks        Show potential attacks
  --show-hourly         Show hourly distribution
  --show-daily          Show daily distribution
```

## Example Usage

### Basic Analysis

```
python log_analyzer.py sample_log.txt
```

This will display a summary of the log file, including:
- Total number of requests
- Date range
- HTTP method distribution
- Status code distribution
- Total bandwidth and average response size
- Top IP addresses and requested paths

### Filtering Logs

```
python log_analyzer.py sample_log.txt --filter-status 404 --filter-ip 192.168.1.200
```

This will analyze only 404 errors from the IP address 192.168.1.200.

### Detecting Attacks

```
python log_analyzer.py sample_log.txt --show-attacks
```

This will display potential attacks or suspicious activity detected in the log file.

### Saving a Report

```
python log_analyzer.py sample_log.txt -o report.json --show-hourly --show-daily --show-attacks
```

This will analyze the log file, display hourly and daily distributions, show potential attacks, and save a comprehensive report to report.json.

## Log Format Support

The analyzer supports the following log formats:

1. **Common Log Format (CLF)**:
   ```
   192.168.1.1 - - [19/Apr/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326
   ```

2. **Combined Log Format**:
   ```
   192.168.1.1 - - [19/Apr/2023:13:55:36 +0000] "GET /index.html HTTP/1.1" 200 2326 "http://example.com" "Mozilla/5.0 ..."
   ```

## Learning Objectives

By studying and modifying this project, students will learn:

1. How to use regular expressions to parse and extract information from text
2. How to handle and analyze date and time data
3. How to create a command-line interface with argument parsing
4. How to generate reports and statistics from log data
5. How to detect patterns and anomalies in data
6. How to organize code using object-oriented programming principles
7. How to handle errors and edge cases in data processing
