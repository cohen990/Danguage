import unittest
from Parser import *

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
		self.assertEqual(result.type, "int")
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
		self.assertEqual(result.type, "string")
	def test_TwoStatementsAssigningToSameVariable_hasLatest(self):
		Parser.parse("int i = 5 \n i = 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 10)
	def test_AssignmentWithAddition_StoresTotalValue(self):
		Parser.parse("int i = 5 + 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 15)
	def test_assignmentWithAdditionFromExistingVariable_StoresFirstValue(self):
		Parser.parse("int i = 5\n int j = 5 + i")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_assignmentWithAdditionFromExistingVariable_StoresSecondValue(self):
		Parser.parse("int i = 5\n int j = 5 + i")
		result = InternalStateProvider.internalVariables["j"]
		self.assertEqual(result.value, 10)

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
	def test_givenNameAndString_AssignsToNameTypeOfString(self):
		Parser.assign("name", "\"string\"")
		result = InternalStateProvider.internalVariables["name"]
		self.assertEqual(result.type, "string")
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

class TestParser_Evaluate(unittest.TestCase):
	def test_givenEmpty_RaisesParserError(self):
		with self.assertRaises(ParserError): Parser.evaluate([])
	def test_givenSingleThing_ReturnsInput(self):
		result = Parser.evaluate(["15"])
		self.assertEqual(result, "15")
	def test_givenAddition_ReturnsAddedThings(self):
		result = Parser.evaluate(["15", "+", "10"])
		self.assertEqual(result, "25")
	def test_givenAdditionWithStoredVariableOnRHS_ReturnsAddedThings(self):
		InternalStateProvider.setVariable("i", "10", "int")
		result = Parser.evaluate(["5", "+", "i"])
		self.assertEqual(result, "15")
	def test_givenAdditionWithStoredVariableOnLHS_ReturnsAddedThings(self):
		InternalStateProvider.setVariable("i", "10", "int")
		result = Parser.evaluate(["i", "+", "10"])
		self.assertEqual(result, "20")
	def test_givenAdditionWithStoredVariableOnBothSides_ReturnsAddedThings(self):
		InternalStateProvider.setVariable("i", "10", "int")
		InternalStateProvider.setVariable("j", "100", "int")
		result = Parser.evaluate(["i", "+", "j"])
		self.assertEqual(result, "110")
	def test_givenAdditionWithStoredVariableOnBothSides_ReturnsAddedThings(self):
		InternalStateProvider.setVariable("i", "10", "int")
		InternalStateProvider.setVariable("j", "100", "int")
		result = Parser.evaluate(["i", "+", "j"])
		self.assertEqual(result, "110")
	def test_givenStringAddition_ReturnsConcatenatedStrings(self):
		result = Parser.evaluate(["\"test1\"", "+", "\"test2\""])
		self.assertEqual(result, "test1test2")

if __name__ == '__main__':
	unittest.main()