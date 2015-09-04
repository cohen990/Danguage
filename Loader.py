import sys

def Load(fileName):
	if not fileName: raise ValueError("Given None or empty string as a path.")
	f = open(fileName)
	lines = f.readlines()

	return "".join(lines)