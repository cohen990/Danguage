import unittest
import BaseObject

class TestBaseObject___init__(unittest.TestCase):
	def test_initializesFunctionsToEmptyList(self):
		example = BaseObject.BaseObject()
		self.assertFalse(example.functions)
	def test_initializesPropertiesToEmptyList(self):
		example = BaseObject.BaseObject()
		self.assertFalse(example.properties)

class TestBaseObject_addFunction(unittest.TestCase):
	def test_givenNone_RaisesTypeError(self):
		example = BaseObject.BaseObject()
		with self.assertRaises(TypeError):
			example.addFunction(None)
	def test_givenString_poops(self):
		example = BaseObject.BaseObject()
		with self.assertRaises(TypeError):
			example.addFunction("poop")
	def test_givenADFunction_AddsToFunctions(self):
		example = BaseObject.BaseObject()
		function = BaseObject.DFunction([], None)
		example.addFunction(function)
		self.assertIn(function, example.functions)