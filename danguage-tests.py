import unittest

class TestLoadMethods(unittest.TestCase):
	def test_load_given_empty_returns_none(self):
		self.assertIsNone(Loader.load(""))

	def test_load_given_missing_file_raises(self):
		with self.assertRaises(IOError):
			Loader.load("poop.dan")

class TestParserMethods(unittest.TestCase):
	def parse_given_empty_returns_nothing(self):
		self.assertIsNone(Parser.parse(""));
	def parse_given_assignment_assigns(self):
		Parser.parse("i = 5")
		result = InternalStateProvider.get("i")
		self.assertEqual(result, 5);

class Loader:
	def load(fileName):
		if(fileName == ""):
			return;
		raise IOError;

class Parser:
	def parse(input):
		return;

class InternalStateProvider:
	def get(key):
		return;

if __name__ == '__main__':
    unittest.main()