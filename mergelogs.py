import os
import re
import sys

from optparse import OptionParser

from subprocess import check_output

# Regex used to match relevant loglines (in this case, a specific IP address)

#
# This code works with a timestamp that looks like this:
# 2018-09-06 15:20:40,980
#
#

parser = OptionParser()
parser.add_option("-f", "--files")
parser.add_option("-o", "--output")

(options, args) = parser.parse_args()

files = options.files.split(',')

#
# This expression work with log files that tart with a date
# I.E. 2018-09-06
#
line_regex = re.compile("^[^0-90-90-90-9\-0-90-9\-0-90-9]")

with open("tmp.log", "w") as out_file:
    for filename in files:
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



sorted = check_output(["/usr/bin/sort", "--key=1,2", "tmp.log"])


os.remove("tmp.log")

lines = sorted.split('\n')
with open(options.output, "w") as out_file:
    for line in lines:
        print "\nBefore " + line
        newline = line.replace('\1', '\n')
        print "After " + newline + "\n"
        out_file.write(newline + "\n")



sys.exit(0)
