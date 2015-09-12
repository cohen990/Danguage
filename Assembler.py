from Loader import *;

class Assembler:
	def __init__(self):
		return

	def GetByteCodeForLine(self, line):
		if line[0].isspace():
			byteCode = []
			isHex = False;
			splitLine = line.split();

			operator, operands = splitLine[0], splitLine[1:]

			if operator == "LDA":
				if not len(operands) == 1:
					raise AssemblerError("'LDA' requires 1 operand")
				byteCode.append('0x01')
			elif operator == "LDX":
				if not len(operands) == 2:
					raise AssemblerError("'LDX' requires 2 operands")
				byteCode.append('0x02')
			elif operator == "STA":
				if not len(operands) == 1:
					raise AssemblerError("'STA' requires 1 operand")
				byteCode.append('0x03')

				if not operands[0] == ",X":
					raise AssemblerError("Unexpected behaviour with STA")

				return byteCode
			elif operator == "END":
				byteCode.append('0x04')

				return byteCode

			for operand in operands:

				if operand[0] == "#": operand = operand[1:] 

				if operand[0] == "$":
					operand = operand[1:]
					isHex = True

				if isHex:
					byteCode.append("0x{:02X}".format(int(operand, 16)))
				else:
					byteCode.append("0x{:02X}".format(int(operand)))


			return byteCode
		return

class AssemblerError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)