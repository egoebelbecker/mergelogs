#!/usr/bin/python
import os
import re
import argparse
from subprocess import check_output


parser = argparse.ArgumentParser(description="Process inout and output file names")
parser.add_argument("-f", "--files", help="list of input files", required=True, nargs='+')
parser.add_argument("-o", "--output", help="output file", required=True, type=argparse.FileType('w'))
args = parser.parse_args()

#
# This expression work with log files that start with a date
# I.E. 2018-09-06
#
line_regex = re.compile("^[^0-90-90-90-9\-0-90-9\-0-90-9]")

with open("tmp.log", "w") as out_file:
    for filename in args.files:
        print "Processing " + filename
        lastline = ""
        with open(filename, "r") as in_file:
            # Loop over each log line
            for line in in_file:
                # If log line matches our regex, print to console, and output file
                if line_regex.search(line):
                    lastline = lastline.rstrip('\n')
                    lastline += '\1'
                    lastline += line
                else:
                    out_file.write(lastline)
                    lastline = line

sorted_log = check_output(["/usr/bin/sort", "--key=1,2", "tmp.log"])

os.remove("tmp.log")

lines = sorted_log.split('\n')
for line in lines:
    newline = line.replace('\1', '\n')
    args.output.write(newline + "\n")

