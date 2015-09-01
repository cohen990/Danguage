import unittest

class TestLoadMethods(unittest.TestCase):
	def test_load_given_empty_returns_none(self):
		self.assertIsNone(Loader.load(""))

	def test_load_given_missing_file_raises(self):
		with self.assertRaises(IOError):
			Loader.load("poop.dan")

class TestParserMethods(unittest.TestCase):
	def test_parse_given_empty_returns_nothing(self):
		self.assertIsNone(Parser.parse(""))
	def test_parse_given_assignment_assigns_5(self):
		Parser.parse("let i be 5")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result, 5)
	def test_parse_given_assignment_assigns_10(self):
		Parser.parse("let i be 10")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result, 10)
	def test_parse_given_string_assignment_assigns_superbowl(self):
		Parser.parse("let sportsEvent be \"superbowl\"")
		result = InternalStateProvider.internalVariables["sportsEvent"]
		self.assertEqual(result, "superbowl")

	def test_getStatements_givenEmptyString_ReturnsEmptyString(self):
		result = Parser.getStatements("")
		self.assertEqual(result, [""])
	def test_getStatements_givenSyntacticallyCorrectSingleStatement_ReturnsSingleStatement(self):
		code = "aisdhpfa asodfhads asdfapodf"
		statement = Parser.getStatements(code)
		self.assertEqual(statement, [code])
	def test_getStatements_givenSyntacticallyCorrectTwoStatements_ReturnsTwoStatements(self):
		expected = ["aisdhpfa asodfhads asdfapodf", "asodfaos asdfoasj asodfjasd"]
		code = "\n".join(expected)
		statements = Parser.getStatements(code)
		self.assertEqual(expected, statements)

	def test_assign_giveniAnd5_Assigns5Toi(self):
		Parser.assign("i", "5")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result, 5)
	def test_assign_giveniAnd15_Assigns15Toi(self):
		Parser.assign("i", "15")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result, 15)
	def test_assign_givenNameAndString_AssignsStringToName(self):
		Parser.assign("name", "\"string\"")
		result = InternalStateProvider.internalVariables["name"]
		self.assertEqual(result, "string")
	def test_assign_givenNameAndDoubleQuotes_AssignsDoubleQuotesToName(self):
		Parser.assign("name", "\"\\\"\\\"\"")
		result = InternalStateProvider.internalVariables["name"]
		self.assertEqual(result, "\\\"\\\"")

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
			codeBlocks = statement.split()
			Parser.assign(key=codeBlocks[1], value=codeBlocks[3])
	def getStatements(code):
		if not code: return [""]
		
		rawStatements = code.split("\n");
		statements = [ statement.strip() for statement in rawStatements if statement]

		return statements

	def assign(key, value):
		if("\"" in value):
			value = value[1:-1]
			InternalStateProvider.set(key, value)
		else:
			InternalStateProvider.set(key, int(value))

class SyntaxError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class InternalStateProvider:
	internalVariables = {}
	def get(key):
		return
	def set(key, value):
		InternalStateProvider.internalVariables[key] = value

if __name__ == '__main__':
	unittest.main()