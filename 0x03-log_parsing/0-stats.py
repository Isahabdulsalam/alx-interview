#!/usr/bin/python3
import sys
import re

# Regular expression to parse log lines
log_pattern = re.compile(
    r'(?P<ip>\S+) - (?P<date>.*?) "(?P<method>\S+) (?P<path>\S+) HTTP/(?P<version>\S+)" (?P<status>\d+) (?P<size>\d+)'
)

# Initialize counters
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = match.group('status')
            size = int(match.group('size'))
            file_size += size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
        else:
            print(f"Failed to parse line: {line.strip()}")
        if line_count % 10 == 0:
            print(f"File size: {file_size}")
            for code, count in sorted(status_codes.items()):
                if count:
                    print(f"{code}: {count}")
finally:
    print(f"File size: {file_size}")
    for code, count in sorted(status_codes.items()):
        if count:
            print(f"{code}: {count}")
