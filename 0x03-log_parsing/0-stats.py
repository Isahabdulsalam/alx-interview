#!/usr/bin/python3
"""A script for parsing logs"""
import re
import sys


def extract_input(input_line):
    """Extracts sections of the log line."""
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*(?P<date>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\d+)',
        r'\s*(?P<file_size>\d+)\s*'
    )
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    info = {'status_code': None, 'file_size': 0}
    
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match:
        info['status_code'] = resp_match.group('status_code')
        info['file_size'] = int(resp_match.group('file_size'))
    
    return info


def print_statistics(total_file_size, status_codes_stats):
    """Prints accumulated statistics of the logs"""
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        if status_codes_stats[status_code] > 0:
            print('{:s}: {:d}'.format(status_code, status_codes_stats[status_code]), flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics based on a single line of log input."""
    line_info = extract_input(line)
    
    if line_info['status_code'] in status_codes_stats:
        status_codes_stats[line_info['status_code']] += 1
    total_file_size += line_info['file_size']
    
    return total_file_size


def run():
    """Runs the main loop for parsing and collecting log data."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(line.strip(), total_file_size, status_codes_stats)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
