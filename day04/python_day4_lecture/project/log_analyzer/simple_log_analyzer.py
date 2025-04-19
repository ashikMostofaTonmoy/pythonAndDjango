import re
from collections import Counter


class SimpleLogAnalyzer:
    def __init__(self):
        self.log_entries = []
        self.ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.date_pattern = r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'
        self.status_pattern = r'"\s(\d{3})\s'

    def read_log_file(self, filename):
        """Read and parse log file"""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    self.log_entries.append(line.strip())
            print(f"Successfully read {len(self.log_entries)} log entries")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found!")

    def count_ips(self):
        """Count occurrences of each IP address"""
        ip_counter = Counter()
        for entry in self.log_entries:
            ip_match = re.search(self.ip_pattern, entry)
            if ip_match:
                ip_counter[ip_match.group()] += 1
        return ip_counter

    def count_status_codes(self):
        """Count occurrences of each status code"""
        status_counter = Counter()
        for entry in self.log_entries:
            status_match = re.search(self.status_pattern, entry)
            if status_match:
                status_counter[status_match.group(1)] += 1
        return status_counter

    def get_requests_by_hour(self):
        """Count requests by hour"""
        hour_counter = Counter()
        for entry in self.log_entries:
            date_match = re.search(self.date_pattern, entry)
            if date_match:
                hour = date_match.group(1).split(':')[0]
                hour_counter[hour] += 1
        return hour_counter

    def print_summary(self):
        """Print a summary of the log analysis"""
        print("\nLog Analysis Summary")
        print("-" * 30)

        # IP Statistics
        print("\nTop 5 IP Addresses:")
        for ip, count in self.count_ips().most_common(5):
            print(f"{ip}: {count} requests")

        # Status Code Statistics
        print("\nStatus Code Distribution:")
        for status, count in self.count_status_codes().most_common():
            print(f"Status {status}: {count} occurrences")

        # Hourly Statistics
        print("\nRequests by Hour:")
        for hour, count in sorted(self.get_requests_by_hour().items()):
            print(f"Hour {hour}: {count} requests")


def main():
    analyzer = SimpleLogAnalyzer()

    while True:
        print("\nSimple Log Analyzer")
        print("1. Load Log File")
        print("2. Show Analysis")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            filename = input("Enter log file name: ")
            analyzer.read_log_file(filename)

        elif choice == "2":
            if not analyzer.log_entries:
                print("No log entries loaded! Please load a log file first.")
            else:
                analyzer.print_summary()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
