#!/usr/bin/python3
import sys
import signal
import re

log_pattern = re.compile(r'(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')
status_counts = {}
total_size = 0
line_count = 0

def print_stats():
    print("Total file size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    try:
        match = log_pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            status_code = int(status_code)
            file_size = int(file_size)

            total_size += file_size
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1
            line_count += 1

        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue
