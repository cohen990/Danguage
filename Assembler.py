from Loader import *;

class Assembler:
	def __init__(self):
		return

	def ValidateArgs(self, operator, operands, numOperands):
		if not len(operands) == numOperands:
			message = "'"+operator+"' requires "+str(numOperands)+" operand"

			if(numOperands > 1):
				message += "s"

			raise AssemblerError(message)


	def GetByteCodeForLine(self, line):
		if line[0].isspace():
			byteCode = []
			isHex = False;
			splitLine = line.split();

			operator, operands = splitLine[0], splitLine[1:]

			if operator == "LDA":
				self.ValidateArgs(operator, operands, 1)
				byteCode.append('0x01')
			elif operator == "LDX":
				self.ValidateArgs(operator, operands, 2)
				byteCode.append('0x02')
			elif operator == "STA":
				self.ValidateArgs(operator, operands, 1)
				byteCode.append('0x03')

				if not operands[0] == ",X":
					raise AssemblerError("Unexpected behaviour with STA")

				return byteCode
			elif operator == "END":
				self.ValidateArgs(operator, operands, 0)
				byteCode.append('0x04')

				return byteCode
			elif operator == "CMPA":
				self.ValidateArgs(operator, operands, 1)
				byteCode.append('0x05')
			elif operator == "CMPB":
				self.ValidateArgs(operator, operands, 1)
				byteCode.append('0x06')
			elif operator == "CMPX":
				self.ValidateArgs(operator, operands, 2)
				byteCode.append('0x07')
			elif operator == "CMPY":
				self.ValidateArgs(operator, operands, 2)
				byteCode.append('0x08')
			elif operator == "CMPD":
				self.ValidateArgs(operator, operands, 2)
				byteCode.append('0x09')
			else:
				raise AssemblerError("Operator not recognised '" + operator + "'.")

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