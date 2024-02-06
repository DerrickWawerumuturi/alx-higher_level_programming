#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
line_count = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_metrics():
    print("Total file size:", total_file_size)
    print("Number of lines by status code:")
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")

def handle_interrupt(signal_number, frame):
    print("\nKeyboard Interrupt")
    print_metrics()
    sys.exit(0)

def process_line(line):
    global total_file_size, line_count, status_code_counts
    parts = line.split()
    file_size = int(parts[-1])
    status_code = int(parts[-2])
    total_file_size += file_size
    line_count += 1
    status_code_counts[status_code] += 1

def main():
    signal.signal(signal.SIGINT, handle_interrupt)
    for line in sys.stdin:
        process_line(line.strip())
        if line_count % 10 == 0:
            print_metrics()
            print()

if __name__ == "__main__":
    main()
