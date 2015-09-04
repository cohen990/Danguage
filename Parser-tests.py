import unittest
from Parser import *
import pdb

class TestParser_Parse(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()

	def test_given_empty_returns_nothing(self):
		self.assertIsNone(self.parser.parse(""))
	def test_given_assignment_assigns_5(self):
		self.parser.parse("int i = 5")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_givenAssignment_assignsiAsAnInt(self):
		self.parser.parse("int i = 5")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.type, "int")
	def test_given_assignment_assigns_10(self):
		self.parser.parse("int i = 10")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 10)
	def test_given_string_assignment_assigns_superbowl(self):
		self.parser.parse("string sportsEvent = \"superbowl\"")
		result = self.stateProvider.internalVariables["sportsEvent"]
		self.assertEqual(result.value, "superbowl")
	def test_givenStringAssignment_assignssportsEventAsString(self):
		self.parser.parse("string sportsEvent = \"superbowl\"")
		result = self.stateProvider.internalVariables["sportsEvent"]
		self.assertEqual(result.type, "string")
	def test_TwoStatementsAssigningToSameVariable_hasLatest(self):
		self.parser.parse("int i = 5 \n i = 10")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 10)
	def test_AssignmentWithAddition_StoresTotalValue(self):
		self.parser.parse("int i = 5 + 10")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 15)
	def test_assignmentWithAdditionFromExistingVariable_StoresFirstValue(self):
		self.parser.parse("int i = 5\n int j = 5 + i")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_assignmentWithAdditionFromExistingVariable_StoresSecondValue(self):
		self.parser.parse("int i = 5\n int j = 5 + i")
		result = self.stateProvider.internalVariables["j"]
		self.assertEqual(result.value, 10)
	def test_twoIndependentAssignments_StoresFirstValue(self):
		self.parser.parse("int i = 5\n int j = 15")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_twoIndependentAssignments_StoresFirstValue(self):
		self.parser.parse("int i = 5\n int j = 15")
		result = self.stateProvider.internalVariables["j"]
		self.assertEqual(result.value, 15)
	def test_complexAssignment_StoresCorrectValue(self):
		self.parser.parse("int i = 5 + 15 + 32 / 16")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 22)
	def test_givenPrintCommand_DoesntThrow(self):
		result=self.parser.parse("print 5")
	def test_givenPrintCommandWithMathematics_DoesntThrow(self):
		result=self.parser.parse("print 5 + 13")
	def test_givenPrintCommandWithConcatenation_DoesntThrow(self):
		result=self.parser.parse("print \"poop\" + \"wee\"")

class TestParser_GetStatements(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()

	def test_givenEmptyString_ReturnsEmptyString(self):
		result = self.parser.getStatements("")
		self.assertEqual(result, [""])
	def test_givenSingleStatement_ReturnsSingleStatement(self):
		code = "aisdhpfa asodfhads asdfapodf"
		statement = self.parser.getStatements(code)
		self.assertEqual(statement, [code])
	def test_TwoStatementsSeparatedByNewline_ReturnsTwo(self):
		expected = ["aisdhpfa asodfhads asdfapodf",
			"asodfaos asdfoasj asodfjasd"]
		code = "\n".join(expected)
		statements = self.parser.getStatements(code)
		self.assertEqual(expected, statements)

class TestParser_Assign(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()

	def test_giveniAnd5_Assigns5Toi(self):
		self.parser.assign("i", "5")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 5)
	def test_giveniAnd15_Assigns15Toi(self):
		self.parser.assign("i", "15")
		result = self.stateProvider.internalVariables["i"]
		self.assertEqual(result.value, 15)
	def test_givenNameAndString_AssignsStringToName(self):
		self.parser.assign("name", "\"string\"")
		result = self.stateProvider.internalVariables["name"]
		self.assertEqual(result.value, "string")
	def test_givenNameAndString_AssignsToNameTypeOfString(self):
		self.parser.assign("name", "\"string\"")
		result = self.stateProvider.internalVariables["name"]
		self.assertEqual(result.type, "string")
	def test_givenNameAndDoubleQuotes_AssignsDoubleQuotesToName(self):
		self.parser.assign("name", "\"\\\"\\\"\"")
		result = self.stateProvider.internalVariables["name"]
		self.assertEqual(result.value, "\\\"\\\"")

class TestParser_GetLeftAndRightOfOperation(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_givenEmptyList_RaiseParserError(self):
		with self.assertRaises(ParserError):
			left, right = self.parser.getLeftAndRightOfOperation([], "=")
	def test_givenListWithoutAssignmentOperator_RaiseParserError(self):
		with self.assertRaises(ParserError):
			self.parser.getLeftAndRightOfOperation(["poop", "wee"], "=")
	def test_givenSimpleAssignment_ReturnsLeft(self):
		inputList = ["i", "=", "5"]
		left, right = self.parser.getLeftAndRightOfOperation(inputList, "=")
		self.assertEqual(left, ["i"])
	def test_givenSimpleAssignment_ReturnsRight(self):
		inputList = ["i", "=", "5"]
		left, right = self.parser.getLeftAndRightOfOperation(inputList, "=")
		self.assertEqual(right, ["5"])
	def test_givenInitialization_ReturnsLeft(self):
		inputList = ["int", "i", "=", "5"]
		left, right = self.parser.getLeftAndRightOfOperation(inputList, "=")
		self.assertEqual(left, ["int", "i"])
	def test_givenComplexAssignment_ReturnsRight(self):
		inputList = ["int", "i", "=", "5", "+", "10"]
		left, right = self.parser.getLeftAndRightOfOperation(inputList, "=")
		self.assertEqual(right, ["5", "+", "10"])

class TestParser_Evaluate(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_givenEmpty_RaisesParserError(self):
		with self.assertRaises(ParserError): self.parser.evaluate([])
	def test_givenSingleThing_ReturnsInput(self):
		result = self.parser.evaluate(["15"])
		self.assertEqual(result, "15")
	def test_givenAddition_ReturnsAddedThings(self):
		result = self.parser.evaluate(["15", "+", "10"])
		self.assertEqual(result, "25")
	def test_givenAdditionWithStoredVariableOnRHS_ReturnsAddedThings(self):
		self.stateProvider.setVariable("i", DInt(10))
		result = self.parser.evaluate(["5", "+", "i"])
		self.assertEqual(result, "15")
	def test_givenAdditionWithStoredVariableOnLHS_ReturnsAddedThings(self):
		self.stateProvider.setVariable("i", DInt(10))
		result = self.parser.evaluate(["i", "+", "10"])
		self.assertEqual(result, "20")
	def test_givenAdditionWithStoredVariableOnBothSides_ReturnsAddedThings(self):
		self.stateProvider.setVariable("i", DInt(10))
		self.stateProvider.setVariable("j", DInt(100))
		result = self.parser.evaluate(["i", "+", "j"])
		self.assertEqual(result, "110")
	def test_givenAdditionWithStoredVariableOnBothSides_ReturnsAddedThings(self):
		self.stateProvider.setVariable("i", DInt(10))
		self.stateProvider.setVariable("j", DInt(100))
		result = self.parser.evaluate(["i", "+", "j"])
		self.assertEqual(result, "110")
	def test_givenStringAddition_ReturnsConcatenatedStrings(self):
		result = self.parser.evaluate(["\"test1\"", "+", "\"test2\""])
		self.assertEqual(result, "\"test1test2\"")
	def test_givenStringAndIntAddition_RaisesTypeError(self):
		with self.assertRaises(TypeError):
			self.parser.evaluate(["\"test1\"", "+", "42"])
	def test_givenBlocksWithoutOperator_RaisesParserError(self):
		with self.assertRaises(ParserError):
			self.parser.evaluate(["test1", "42"])
	def test_intSubtraction_Subtracts(self):
		result = self.parser.evaluate(["32", "-", "42"])
		self.assertEqual(result, "-10")
	def test_stringSubtraction_RaisesTypeError(self):
		with self.assertRaises(TypeError):
			self.parser.evaluate(["\"poopstorm\"", "-", "\"poop\""])
	def test_intMultiplication_Multiplies(self):
		result = self.parser.evaluate(["5", "*", "3"])
		self.assertEqual(result, "15")
	def test_intDivision_DividesAndReturnsClosestInt(self):
		result = self.parser.evaluate(["5", "/", "3"])
		self.assertEqual(result, "1")
	def test_chainedAdditions_PerformsBothAdditions(self):
		result = self.parser.evaluate(["5", "+", "4", "+", "3"])
		self.assertEqual(result, "12")
	def test_additionThenDivision_PerformsDivisionThenAddition(self):
		result = self.parser.evaluate(["5", "+", "6", "/", "3"])
		self.assertEqual(result, "7")
	def test_divisionThenAddition_PerformsDivisionThenAddition(self):
		result = self.parser.evaluate(["6", "/", "3", "+", "5"])
		self.assertEqual(result, "7")

class TestParser_EvaluateOperator(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()

	def test_givenNoneCodeBlocks_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.parser.evaluateOperator(
				codeBlocks = None, targetOperator = "+")
	def test_givenNone_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.parser.evaluateOperator(
				codeBlocks = ["5", "+", "3"], targetOperator = None)
	def test_givenEmptyCodeBlocks_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.parser.evaluateOperator(
				codeBlocks = [], targetOperator = "+")
	def test_givenCodeBlocksWithoutTargetOperator_RaisesParserError(self):
		with self.assertRaises(ParserError):
			self.parser.evaluateOperator(
				codeBlocks = ["5", "2"], targetOperator = "+")
	def test_given5Plus2_Returns7(self):
		result = self.parser.evaluateOperator(
			codeBlocks = ["5", "+", "2"], targetOperator = "+")
		self.assertEqual(result, ["7"])
	def test_given6Divided2_Returns3(self):
		result = self.parser.evaluateOperator(
			codeBlocks = ["6", "/", "2"], targetOperator = "/")
		self.assertEqual(result, ["3"])
	def test_given6Divided2Plus3WithTargetDivide_Returns3(self):
		result = self.parser.evaluateOperator(
			codeBlocks = ["6", "/", "2", "+", "3"], targetOperator = "/")
		self.assertEqual(result, ["3", "+", "3"])
	def test_given6Divided2Plus3WithTargetPlus_Returns5(self):
		result = self.parser.evaluateOperator(
			codeBlocks = ["6", "/", "2", "+", "3"], targetOperator = "+")
		self.assertEqual(result, ["6", "/", "5"])

class TestParser_InferType(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_givenObjectWithEmptyValue_SetsTypeToNull(self):
		result = self.parser.inferType(None)
		self.assertEqual(result.type, "null")
	def test_givenObjectWithEmptyValue_SetsValueToNone(self):
		result = self.parser.inferType(None)
		self.assertIsNone(result.value)
	def test_givenObjectWithNumber_DoesntModifyValue(self):
		result = self.parser.inferType("15")
		self.assertEqual(result.value, 15)
	def test_givenObjectWithNumber_SetsTypeToInt(self):
		result = self.parser.inferType("15")
		self.assertEqual(result.type, "int")
	def test_givenObjectWithString_SetsTypeToString(self):
		result = self.parser.inferType("\"batmobile\"")
		self.assertEqual(result.type, "string")

class TestParser_GetTokens(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
		self.parser = Parser(self.stateProvider)
	def tearDown(self):
		self.stateProvider.clearState()

	def test_givenNoneStatement_RaiseValueError(self):
		with self.assertRaises(ValueError):
			self.parser.getTokens(None)
	def test_givenEmptyStatement_RaiseValueError(self):
		with self.assertRaises(ValueError):
			self.parser.getTokens("")
	def test_givenSpacedOutStatement_ReturnsTokens(self):
		result = self.parser.getTokens("int i = 5")
		self.assertEqual(result, ["int", "i", "=", "5"])
	def test_givenStringWithWhitespace_ReturnsStringIntact(self):
		result = self.parser.getTokens(r'"test string"')
		self.assertEqual(result, [r'"test string"'])
	def test_givenStringWithWhitespace_ReturnsStringIntact(self):
		result = self.parser.getTokens(r'"\"hello, world!\""')
		self.assertEqual(result, [r'"\"hello, world!\""'])

class TestParserError___str__(unittest.TestCase):
	def test_initializedWithEmptyString_ReturnsName(self):
		error = ParserError("")
		self.assertEqual(str(error), "''");
	def test_initializedWithUnableToParse_ReturnsUnableToParse(self):
		error = ParserError("Unable to parse")
		self.assertEqual(str(error), "'Unable to parse'");

if __name__ == "__main__":
	unittest.main()