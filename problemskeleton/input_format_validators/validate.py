#!/usr/bin/env python3

import sys
import re

n_line = sys.stdin.readline()
print(repr(n_line)) # useful for debugging to see where we have read
assert re.match('^[1-9][0-9]*\n$', n_line) # note: no leading zeros
n = int(n_line)
'''
CHANGED FOR 1 <= n <= 1_000_000 
'''
assert 1 <= n <= 1_000_000 #range check

# Read 2nd line
numbers_line = sys.stdin.readline()
print(repr(numbers_line))  # useful for debugging

# Split numbers
numbers = numbers_line.strip().split()
assert len(numbers) == n # must have exactly n nbs

for num in numbers:
    assert re.match('^(0|[1-9][0-9]{0,4})$', num)
    x = int(num)
    assert 0 <= x <= 10000
    
# ensure no extra input
assert sys.stdin.readline() == ''

# if we get here, all is well; use exit code 42.
sys.exit(42)

