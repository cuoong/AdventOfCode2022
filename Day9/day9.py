import sys

file = sys.argv[1] if len(sys.argv) > 1 else '9.in'
data = open(file).readlines()

line = [x.strip() for x in data]
