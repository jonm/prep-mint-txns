#!/usr/bin/env python
# Copyright (C) 2018 Jonathan T. Moore

import csv
import datetime
import sys

def excerpt_month(in_f, out_f, month, year):
    reader = csv.reader(in_f)
    writer = csv.writer(out_f)
    first = True
    for row in reader:
        if first:
            writer.writerow(row)
            first = False
            continue
        d = datetime.datetime.strptime(row[0], "%m/%d/%Y")
        if d.month == month and d.year == year:
            writer.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
    else:
        now = datetime.datetime.now()
        month = now.month
        year = now.year
    excerpt_month(sys.stdin, sys.stdout, month, year)
