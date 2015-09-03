from InternalStateProvider import *
import re

class Parser:
	def __init__(self, stateProvider):
		self.stateProvider = stateProvider

	def parse(self, code):
		if(code == ""): return
		statements = self.getStatements(code=code)
		for statement in statements:
			if("=" in statement):
				self.parseAssignmentStatement(statement)

	def getStatements(self, code):
		if not code: return [""]
		
		rawStatements = code.split("\n");
		statements = [ statement.strip() for statement in rawStatements 
			if statement]

		return statements

	def parseAssignmentStatement(self, statement):
		codeBlocks = statement.split()

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
		if not codeBlocks or operator not in codeBlocks:
			raise ParserError(
				"An invalid statement has been passed into the self.")

		indexOfEquals = codeBlocks.index(operator)
		leftHandSide = codeBlocks[0:indexOfEquals]
		rightHandSide = codeBlocks[indexOfEquals + 1:]
		return leftHandSide, rightHandSide

	def assign(self, key, value):
		temp = self.inferType(Object(value, "type-unknown"))
		self.stateProvider.setVariable(key, temp)
	
	def evaluate(self, blocks):
		if not blocks: raise ParserError("Empty list passed to Evaluate")
		if len(blocks) == 1: return blocks[0]

		operators = [operator for operator in self.stateProvider.operators
			if operator in blocks]

		if operators:
			left, right = self.getLeftAndRightOfOperation(blocks, operators[0])

			left = self.stateProvider.tryLookup(left[0])
			right = self.stateProvider.tryLookup(right[0])

			if not isinstance(right, Object):
				right = self.inferType(Object(right, "type-unknown"))
			if not isinstance(left, Object):
				left = self.inferType(Object(left, "type-unknown"))

			operation = operators[0]

			if not operation in left.operators:
				raise TypeError("Cant poop")

			return str(left.operators[operation](right.value))

		raise ParserError("No operator found in statement.")

	def inferType(self, untypedObject):
		if untypedObject.value is None: return Object(None, "null")
		if "\"" in untypedObject.value: 
			return DString(untypedObject.value)
		return DInt(untypedObject.value)

class ParserError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)