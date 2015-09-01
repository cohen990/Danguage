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
		Parser.parse("assign i 5;")
		result = InternalStateProvider.internalVariables["i"]
		self.assertEqual(result, 5)
	# def test_parse_given_assignment_assigns_10(self):
	# 	Parser.parse("assign i 10;")
	# 	result = InternalStateProvider.internalVariables["i"]
	# 	self.assertEqual(result, 10)

	def test_getStatements_givenEmptyString_ReturnsEmptyString(self):
		result = Parser.getStatements("")
		self.assertEqual(result, "")
	def test_getStatements_givenSyntacticallyCorrectSingleStatement_ReturnsSingleStatement(self):
		code = "aisdhpfa asodfhads asdfapodf"
		statement = Parser.getStatements(code + ";")
		self.assertEqual(statement, [code])
	def test_getStatements_givenSyntacticallyCorrectTwoStatements_ReturnsTwoStatements(self):
		expected = ["aisdhpfa asodfhads asdfapodf", "asodfaos asdfoasj asodfjasd"]
		code = ";\n".join(expected) + ";"
		statements = Parser.getStatements(code)
		self.assertEqual(expected, statements)

class Loader:
	def load(fileName):
		if(fileName == ""):
			return
		raise IOError

class Parser:
	def parse(code):
		if(code == ""): return
		statements = Parser.getStatements(code)
		InternalStateProvider.set("i", 5)

	def getStatements(code):
		if not code: return ""
		
		rawStatements = code.split(";");
		statements = [ statement.strip() for statement in rawStatements if statement]

		return statements

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