#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys

def main():
  total_size = 0
  status_code_counts = {}

  for line in sys.stdin:
    line = line.strip()
    ip_address, date, request, status_code, file_size = line.split()

    total_size += int(file_size)

    if status_code not in status_code_counts:
      status_code_counts[status_code] = 0

    status_code_counts[status_code] += 1

    if len(status_code_counts) % 10 == 0 or sys.stdin.isatty():
      print("Total file size:", total_size)
      for status_code, count in sorted(status_code_counts.items()):
        print(status_code, ":", count)

if __name__ == "__main__":
  main()
