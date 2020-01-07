#! /usr/bin/python3

import sys

for i, c in enumerate(sys.argv[1].encode("utf-8", errors="surrogateescape")):
	print(chr(c - i), end='')
print()
