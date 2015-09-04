from InternalStateProvider import *
import re

class Parser:
	def __init__(self, stateProvider):
		self.stateProvider = stateProvider

	def parse(self, code):
		if(code == ""): return
		statements = self.getStatements(code=code)
		for statement in statements:
			if statement.startswith("print "):
				self.DPrint(statement)
			elif "=" in statement:
				self.parseAssignmentStatement(statement)

	def DPrint(self, code):
		codeBlocks = self.getTokens(code)
		del codeBlocks[0]
		result = self.evaluate(codeBlocks)
		print(result)

	def getStatements(self, code):
		if not code: return [""]
		
		rawStatements = code.split("\n");
		statements = [ statement.strip() for statement in rawStatements 
			if statement]

		return statements

	def getTokens(self, statement, debug = False):
		if not statement: raise ValueError("statement is null or empty")
		if debug: print("\nstatement: " +  statement)
		discoveredTokens = []
		lastIndex = 0
		inString = False
		escaped = False

		for index, character in enumerate(statement):
			toggleString = False
			if debug: print("######\nchar: ", character)
			if debug: print("char == \\\\: ", character == "\\")
			if debug: print("inString: ", inString)
			if character == "\\": escaped = not escaped
			if debug: print("escaped: ", escaped)
			if not escaped and character == "\"":
				toggleString = True
			if debug: print("toggleString: ", toggleString)

			if toggleString:
				inString = not inString
				toggleString = False
			if character.isspace() and not inString:
				discoveredTokens.append(statement[lastIndex:index])
				lastIndex = index + 1

		discoveredTokens.append(statement[lastIndex:])

		return discoveredTokens

	def parseAssignmentStatement(self, statement):
		codeBlocks = self.getTokens(statement)

		leftHandSide, rightHandSide = self.getLeftAndRightOfOperation(
			codeBlocks, '=')

		rightHandSideValue = rightHandSide[0]

		if(len(rightHandSide) > 1):
			rightHandSideValue = self.evaluate(rightHandSide)

		if(leftHandSide[0] in self.stateProvider.knownTypes):
			self.assign(key=leftHandSide[1], value=rightHandSideValue)
		else:
			self.assign(key=leftHandSide[0], value=rightHandSideValue)

	def getLeftAndRightOfOperation(self, codeBlocks, operator):
		if not codeBlocks:
			raise ParserError(
				"An empty statement has been passed into the parser.")
		if operator not in codeBlocks:
			raise ParserError(
				"No operator found in code: " + str(codeBlocks))

		indexOfEquals = codeBlocks.index(operator)
		leftHandSide = codeBlocks[0:indexOfEquals]
		rightHandSide = codeBlocks[indexOfEquals + 1:]
		return leftHandSide, rightHandSide

	def assign(self, key, value):
		temp = self.inferType(value)
		self.stateProvider.setVariable(key, temp)
	
	def evaluate(self, blocks):
		if not blocks: raise ParserError("Empty list passed to Evaluate")
		if len(blocks) == 1: return blocks[0]

		operators = [operator for operator in self.stateProvider.operators
			if operator in blocks]

		if not operators: raise ParserError("No operator found in statement.")

		while("/" in blocks):
			blocks = self.evaluateOperator(blocks, "/")

		while("*" in blocks):
			blocks = self.evaluateOperator(blocks, "*")

		while("+" in blocks):
			blocks = self.evaluateOperator(blocks, "+")

		while("-" in blocks):
			blocks = self.evaluateOperator(blocks, "-")

		return blocks[0]
		
	def evaluateOperator(self, codeBlocks, targetOperator):
		if not codeBlocks or not targetOperator:
			raise ValueError("Cannot evaluate 'None'")
		if targetOperator not in codeBlocks:
			raise ParserError(
				"Operator '"+targetOperator+
				"' not found in " + str(codeBlocks) + ".")

		indexOfOperator = codeBlocks.index(targetOperator)


		left = self.stateProvider.tryLookup(codeBlocks[indexOfOperator - 1])
		right = self.stateProvider.tryLookup(codeBlocks[indexOfOperator + 1])

		if not isinstance(right, Object):
			right = self.inferType(right)
		if not isinstance(left, Object):
			left = self.inferType(left)

		if not targetOperator in left.operators:
			raise TypeError(
				"Object of type '" + left.type +
				"' does not define operator '"+ targetOperator + "'.")

		result = str(left.operators[targetOperator](right.value))

		del codeBlocks[indexOfOperator + 1]
		del codeBlocks[indexOfOperator - 1]

		codeBlocks[indexOfOperator - 1] = result

		return codeBlocks

	def inferType(self, untypedObject):
		if untypedObject is None: return Object(None, "null")
		if "\"" in str(untypedObject): 
			return DString(untypedObject)
		return DInt(untypedObject)

class ParserError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)