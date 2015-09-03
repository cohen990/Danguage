import unittest
from InternalStateProvider import *
from Types import *
import pdb

class TestInternalStateProvider_tryLookup(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
	def tearDown(self):
		self.stateProvider.clearState()

	def test_givenEmpty_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.stateProvider.tryLookup("")
	def test_givenKeyNotPresent_returnsKey(self):
		self.stateProvider.clearState()
		result = self.stateProvider.tryLookup("key")
		self.assertEqual(result, "key")
	def test_givenKeyPresent_returnsValue(self):
		self.stateProvider.internalVariables["key"] = Object("15", "int")
		result = self.stateProvider.tryLookup("key")
		self.assertEqual(result.value, "15")
	def test_givenKeyPresent_returnsType(self):
		self.stateProvider.internalVariables["key"] = Object("15", "int")
		result = self.stateProvider.tryLookup("key")
		self.assertEqual(result.type, "int")

class TestInternalStateProvider_getVariable(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_givenEmpty_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.stateProvider.getVariable("")
	def test_givenKeyNotPresent_raisesKeyError(self):
		with self.assertRaises(KeyError):
			self.stateProvider.getVariable("key")
	def test_givenKeyPresent_returnsValue(self):
		self.stateProvider.internalVariables["key"] = Object("15", "int")
		result = self.stateProvider.getVariable("key")
		self.assertEqual(result.value, "15")
	def test_givenKeyPresent_returnsType(self):
		self.stateProvider.internalVariables["key"] = Object("15", "int")
		result = self.stateProvider.getVariable("key")
		self.assertEqual(result.type, "int")

class TestInternalStateProvider_clearState(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_removesVariablesFromInternalState(self):
		self.stateProvider.internalVariables["key"] = Object("15", "int")
		self.stateProvider.clearState()		
		self.assertEqual(len(self.stateProvider.internalVariables), 0)

class TestInternalStateProvider_setVariable(unittest.TestCase):
	def setUp(self):
		self.stateProvider = InternalStateProvider()
	def tearDown(self):
		self.stateProvider.clearState()
		
	def test_setTwo_FirstIsCorrect(self):
		self.stateProvider.setVariable("key1", DInt(5))
		self.stateProvider.setVariable("key2", DInt(10))
		result = self.stateProvider.internalVariables["key1"]
		self.assertEqual(result.value, 5)
	def test_setTwo_SecondIsCorrect(self):
		self.stateProvider.setVariable("key1", DInt(5))
		self.stateProvider.setVariable("key2", DInt(10))
		result = self.stateProvider.internalVariables["key2"]
		self.assertEqual(result.value, 10)
		
	def test_setTwoWithTryLookupInBetween_FirstIsCorrect(self):
		self.stateProvider.setVariable("key1", DInt(5))
		self.stateProvider.tryLookup("key1")
		self.stateProvider.setVariable("key2", DInt(10))
		result = self.stateProvider.internalVariables["key1"]
		self.assertEqual(result.value, 5)
	def test_setTwoWithTryLookupInBetween_SecondIsCorrect(self):
		self.stateProvider.setVariable("key1", DInt(5))
		self.stateProvider.tryLookup("key1")
		self.stateProvider.setVariable("key2", DInt(10))
		result = self.stateProvider.internalVariables["key2"]
		self.assertEqual(result.value, 10)


if __name__ == '__main__':
	unittest.main()