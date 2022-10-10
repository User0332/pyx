from sys import argv
from re import findall

file: str = argv[1]

with open(file, 'r') as f:
	code = f.read()

new_code = ""

while 1:
	start_pyx = code.index("<pyx>")
