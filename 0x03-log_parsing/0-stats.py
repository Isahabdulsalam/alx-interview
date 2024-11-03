#!/usr/bin/python3
"""
Script to parse logs and generate statistics.
"""
import sys
import re

def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_log_line(line):
    """
    Parse a log line and extract status code and file size.
    Expected format:
    166.152.170.40 - [2017-02-05 23:28:50.535640] "GET /projects/260 HTTP/1.1" 200 939
    """
    log_format = re.compile(
        r'(?P<ip>\S+) - (?P<date>[^]+) "(?P<method>\S+) (?P<path>\S+) '
        r'(?P<protocol>\S+)" (?P<status>\d{3}) (?P<size>\d+)')
    match = log_format.match(line)
    if match:
        return int(match.group('status')), int(match.group('size'))
    else:
        return None, None

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            status, size = parse_log_line(line)
            if status and size is not None:
                total_size += size
                if status in status_codes:
                    status_codes[status] += 1
                else:
                    status_codes[status] = 1
                count += 1

            if count == 10:
                print_stats(total_size, status_codes)
                count = 0

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
    print_stats(total_size, status_codes)
