import unittest
from Types import *

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

class TestDInt___init__(unittest.TestCase):
	def test_givenNone_RaisesTypeError(self):
		with self.assertRaises(TypeError):
			thisInt = DInt(None)
	def test_givenString_RaisesValueError(self):
		with self.assertRaises(ValueError):
			thisInt = DInt("string")
	def test_givenInt_StoresInt(self):
		thisInt = DInt("15")
		self.assertEqual(thisInt.value, 15)
	def test_givenInt_HasOperatorPlus(self):
		thisInt = DInt("15")
		self.assertIn("+", thisInt.operators)
	def test_givenInt_HasAccessibleAddClosure(self):
		thisInt = DInt("15")
		operator = thisInt.operators["+"]
		self.assertIsNotNone(operator)
	def test_givenInt_HasUsableAddClosure(self):
		thisInt = DInt("1")
		operator = thisInt.operators["+"]
		self.assertIsNotNone(operator(2))
	def test_givenInt_HasUsableAddClosureThatAddsTwoValues(self):
		thisInt = DInt("1")
		operator = thisInt.operators["+"]
		self.assertEqual(operator(2), 3)
	def test_givenInt_HasSubtractThatSubtractsTwoValues(self):
		thisInt = DInt("1")
		operator = thisInt.operators["-"]
		self.assertEqual(operator(2), -1)
	def test_givenInt_HasMultiplyThatMultipliesTwoValues(self):
		thisInt = DInt("3")
		operator = thisInt.operators["*"]
		self.assertEqual(operator(2), 6)
	def test_givenInt_HasDivideThatDividesTwoValues(self):
		thisInt = DInt("3")
		operator = thisInt.operators["/"]
		self.assertEqual(operator(2), 1)

class TestDString___init__(unittest.TestCase):
	def test_givenNone_RaisesTypeError(self):
		with self.assertRaises(TypeError):
			DString(None)
	def test_givenString_StripsEcapesQuotes(self):
		string = DString("\"test\"")
		self.assertEqual(string.value, "test")
	def test_givenInt_StoresString(self):
		string = DString(15)
		self.assertEqual(string.value, "15")
	def test_givenInt_StoresAddOperator(self):
		string = DString(15)
		self.assertIn("+", string.operators)
	def test_givenString_CanAddAnotherString(self):
		string = DString("\"test1\"")
		operator = string.operators["+"]
		self.assertEqual(operator("\"test2\""), "test1test2")

if __name__ == "__main__":
	unittest.main()