import Loader
import unittest

class TestLoader_Load(unittest.TestCase):
	def test_givenNone_RaisesValueError(self):
		with self.assertRaises(ValueError):
			Loader.Load(None)
	def test_givenEmptyString_RaisesValueError(self):
		with self.assertRaises(ValueError):
			Loader.Load("")
	def test_givenFileThatDoesntExist_RaisesIOError(self):
		with self.assertRaises(IOError):
			Loader.Load("notexistingfile")
	def test_givenExistingEmptyFile_ReturnsEmptyString(self):
		result = Loader.Load("EmptyTest.txt")
		self.assertFalse(result)
	def test_givenExistingFile_ReturnsContent(self):
		result = Loader.Load("ContentTest.txt")
		self.assertEqual(result, "I have content\n")