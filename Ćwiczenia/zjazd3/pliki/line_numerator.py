import sys

with open(sys.argv[1], "r") as fh:
    for i, line in enumerate(fh.readlines()):
        print(i + 1, line, end="")
