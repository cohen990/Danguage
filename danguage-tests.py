import unittest
# import pdb #-> put this in as a break point "pdb.set_trace()"

class TestLoadMethods(unittest.TestCase):
	def test_load_given_empty_returns_none(self):
		self.assertIsNone(Loader.load(""))

	def test_load_given_missing_file_raises(self):
		with self.assertRaises(IOError):
			Loader.load("poop.dan")

class TestParser_Parse(unittest.TestCase):
	def test_given_empty_returns_nothing(self):
		self.assertIsNone(Parser.parse(""))
	def test_given_assignment_assigns_5(self):
		Parser.parse("int i = 5")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_givenAssignment_assignsiAsAnInt(self):
		Parser.parse("int i = 5")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.objectType, "int")
	def test_given_assignment_assigns_10(self):
		Parser.parse("int i = 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 10)
	def test_given_string_assignment_assigns_superbowl(self):
		Parser.parse("string sportsEvent = \"superbowl\"")
		result = InternalStateProvider.internalVariables["sportsEvent"]
		self.assertEqual(result.value, "superbowl")
	def test_givenStringAssignment_assignssportsEventAsString(self):
		Parser.parse("string sportsEvent = \"superbowl\"")
		result = InternalStateProvider.internalVariables["sportsEvent"]
		self.assertEqual(result.objectType, "string")
	def test_TwoStatementsAssigningToSameVariable_hasLatest(self):
		Parser.parse("int i = 5 \n i = 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 10)
	def test_AssignmentWithAddition_StoresTotalValue(self):
		Parser.parse("int i = 5 + 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 15)

class TestParser_GetStatements(unittest.TestCase):
	def test_givenEmptyString_ReturnsEmptyString(self):
		result = Parser.getStatements("")
		self.assertEqual(result, [""])
	def test_givenSingleStatement_ReturnsSingleStatement(self):
		code = "aisdhpfa asodfhads asdfapodf"
		statement = Parser.getStatements(code)
		self.assertEqual(statement, [code])
	def test_TwoStatementsSeparatedByNewline_ReturnsTwo(self):
		expected = ["aisdhpfa asodfhads asdfapodf",
			"asodfaos asdfoasj asodfjasd"]
		code = "\n".join(expected)
		statements = Parser.getStatements(code)
		self.assertEqual(expected, statements)

class TestParser_Assign(unittest.TestCase):
	def test_giveniAnd5_Assigns5Toi(self):
		Parser.assign("i", "5")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_giveniAnd15_Assigns15Toi(self):
		Parser.assign("i", "15")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 15)
	def test_givenNameAndString_AssignsStringToName(self):
		Parser.assign("name", "\"string\"")
		result = InternalStateProvider.internalVariables["name"]
		self.assertEqual(result.value, "string")
	def test_givenNameAndDoubleQuotes_AssignsDoubleQuotesToName(self):
		Parser.assign("name", "\"\\\"\\\"\"")
		result = InternalStateProvider.internalVariables["name"]
		self.assertEqual(result.value, "\\\"\\\"")

class TestParser_GetLeftAndRightOfOperation(unittest.TestCase):
	def test_givenEmptyList_RaiseParserError(self):
		with self.assertRaises(ParserError):
			left, right = Parser.getLeftAndRightOfOperation([], '=')
	def test_givenListWithoutAssignmentOperator_RaiseParserError(self):
		with self.assertRaises(ParserError):
			Parser.getLeftAndRightOfOperation(["poop", "wee"], '=')
	def test_givenSimpleAssignment_ReturnsLeft(self):
		inputList = ["i", "=", "5"]
		left, right = Parser.getLeftAndRightOfOperation(inputList, '=')
		self.assertEqual(left, ["i"])
	def test_givenSimpleAssignment_ReturnsRight(self):
		inputList = ["i", "=", "5"]
		left, right = Parser.getLeftAndRightOfOperation(inputList, '=')
		self.assertEqual(right, ["5"])
	def test_givenInitialization_ReturnsLeft(self):
		inputList = ["int", "i", "=", "5"]
		left, right = Parser.getLeftAndRightOfOperation(inputList, '=')
		self.assertEqual(left, ["int", "i"])
	def test_givenComplexAssignment_ReturnsRight(self):
		inputList = ["int", "i", "=", "5", "+", "10"]
		left, right = Parser.getLeftAndRightOfOperation(inputList, '=')
		self.assertEqual(right, ["5", "+", "10"])

class TestEvaluator_Evaluate(unittest.TestCase):
	def test_givenEmpty_RaisesParserError(self):
		with self.assertRaises(ParserError): Evaluator.evaluate([])
	def test_givenSingleThing_ReturnsInput(self):
		result = Evaluator.evaluate(["15"])
		self.assertEqual(result, "15")
	def test_givenAddition_ReturnsAddedThings(self):
		result = Evaluator.evaluate(["15", "+", "10"])
		self.assertEqual(result, "25")

class Loader:
	def load(fileName):
		if(fileName == ""):
			return
		raise IOError

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
			rightHandSideValue = Evaluator.evaluate(rightHandSide)

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

class SyntaxError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)
class ParserError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InternalStateProvider:
	internalVariables = {}
	knownTypes = ["int", "string"]
	operators = ["+"]
	def getVariable(key):
		return
	def setVariable(key, value, objectType):
		InternalStateProvider.internalVariables[key] = Object(value, objectType)

class Evaluator:
	def evaluate(blocks):
		if not blocks: raise ParserError("Empty list passed to Evaluate")
		if len(blocks) == 1: return blocks[0]

		operators = [operator for operator in InternalStateProvider.operators
			if operator in blocks]

		if operators:
			left, right = Parser.getLeftAndRightOfOperation(blocks, operators[0])
			return str(int(left[0]) + int(right[0]))

		raise ParserError("No operator found in statement.")

class Object:
	def __init__(self, value, objectType):
		self.value = value
		self.objectType = objectType

if __name__ == '__main__':
	unittest.main()