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
	def test_givenString_RaisesTypeError(self):
		example = BaseObject.BaseObject()
		with self.assertRaises(TypeError):
			example.addFunction("poop")
	def test_givenADFunction_AddsToFunctions(self):
		example = BaseObject.BaseObject()
		function = BaseObject.DFunction("exampleFunction", [], None)
		example.addFunction(function)
		self.assertIn(function, example.functions)

class TestBaseObject_addProperty(unittest.TestCase):
	def test_givenNone_RaisesTypeError(self):
		example = BaseObject.BaseObject()
		with self.assertRaises(TypeError):
			example.addProperty(None)
	def test_givenString_RaisesTypError(self):
		example = BaseObject.BaseObject()
		with self.assertRaises(TypeError):
			example.addFunction("poop")
	def test_givenADFunction_AddsToFunctions(self):
		example = BaseObject.BaseObject()
		dProperty = BaseObject.DProperty([], None)
		example.addProperty(dProperty)
		self.assertIn(dProperty, example.properties)