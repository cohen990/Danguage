from InternalStateProvider import *
import re

class Parser:
	def parse(code):
		if(code == ""): return
		statements = Parser.getStatements(code=code)
		for statement in statements:
			if("=" in statement):
				Parser.parseAssignmentStatement(statement)

	def getStatements(code):
		if not code: return [""]
		
		rawStatements = code.split("\n");
		statements = [ statement.strip() for statement in rawStatements 
			if statement]

		return statements

	def parseAssignmentStatement(statement):
		codeBlocks = statement.split()

		leftHandSide, rightHandSide = Parser.getLeftAndRightOfOperation(
			codeBlocks, '=')

		rightHandSideValue = rightHandSide[0]

		if(len(rightHandSide) > 1):
			rightHandSideValue = Parser.evaluate(rightHandSide)

		if(leftHandSide[0] in InternalStateProvider.knownTypes):
			Parser.assign(key=leftHandSide[1], value=rightHandSideValue)
		else:
			Parser.assign(key=leftHandSide[0], value=rightHandSideValue)

	def getLeftAndRightOfOperation(codeBlocks, operator):
		if not codeBlocks or operator not in codeBlocks:
			raise ParserError(
				"An invalid statement has been passed into the parser.")

		indexOfEquals = codeBlocks.index(operator)
		leftHandSide = codeBlocks[0:indexOfEquals]
		rightHandSide = codeBlocks[indexOfEquals + 1:]
		return leftHandSide, rightHandSide

	def assign(key, value):
		if("\"" in value):
			value = value[1:-1]
			InternalStateProvider.setVariable(key, value, "string")
		else:
			InternalStateProvider.setVariable(key, int(value), "int")

	def evaluate(blocks):
		if not blocks: raise ParserError("Empty list passed to Evaluate")
		if len(blocks) == 1: return blocks[0]

		operators = [operator for operator in InternalStateProvider.operators
			if operator in blocks]

		if operators:
			left, right = Parser.getLeftAndRightOfOperation(blocks, operators[0])

			left = InternalStateProvider.tryLookup(left[0])
			right = InternalStateProvider.tryLookup(right[0])

			if isinstance(right, Object): right = right.value
			if isinstance(left, Object): left = left.value

			return str(int(left) + int(right))

		raise ParserError("No operator found in statement.")

class ParserError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)