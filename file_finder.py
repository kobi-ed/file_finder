# /usr/bin/env python 3

# Implementation of the file_finder.py program
# Locates a file in the current directory
# Based on the os.walk() function
# Copied from Python Projects by Laura Cassel and Alan Gauld
import os, re
import os.path as path

def find_file(pattern, base='.'):
    """Find the file in base based on the given pattern.
    Return a list of the matched files."""

    regex = re.compile(pattern)
    matches = []

    for root, dirs, files in os.walk(base):
        for f in files:
            if regex.match(f):
                matches.append(path.join(base, f))
    return matches
