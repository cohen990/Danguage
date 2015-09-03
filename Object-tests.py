import unittest
from Object import *

class TestObject___str__(unittest.TestCase):
	def test_initializedWithEmptyValueAndEmptyType_ReturnsEmptyEverything(self):
		thisObject = Object("", "")
		self.assertEqual(str(thisObject), " <>")
	def test_initializedWith15AndInt_Returns15_int(self):
		thisObject = Object("15", "int")
		self.assertEqual(str(thisObject), "15 <int>")

class TestObject___repr__(unittest.TestCase):
	def test_initializedWithEmptyValueAndEmptyType_ReturnsEmptyEverything(self):
		thisObject = Object("", "")
		self.assertEqual(repr(thisObject), " <>")
	def test_initializedWith15AndInt_Returns15_int(self):
		thisObject = Object("15", "int")
		self.assertEqual(repr(thisObject), "15 <int>")
