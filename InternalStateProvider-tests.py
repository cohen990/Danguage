import unittest
from InternalStateProvider import *
from Object import *
import pdb

class TestInternalStateProvider_tryLookup(unittest.TestCase):
	def test_givenEmpty_RaisesValueError(self):
		with self.assertRaises(ValueError):
			InternalStateProvider.tryLookup("")
	def test_givenKeyNotPresent_returnsKey(self):
		InternalStateProvider.clearState()
		result = InternalStateProvider.tryLookup("key")
		self.assertEqual(result, "key")
	def test_givenKeyPresent_returnsValue(self):
		InternalStateProvider.internalVariables["key"] = Object("15", "int")
		result = InternalStateProvider.tryLookup("key")
		self.assertEqual(result.value, "15")
	def test_givenKeyPresent_returnsType(self):
		InternalStateProvider.internalVariables["key"] = Object("15", "int")
		result = InternalStateProvider.tryLookup("key")
		self.assertEqual(result.type, "int")

class TestInternalStateProvider_getVariable(unittest.TestCase):
	def test_givenEmpty_RaisesValueError(self):
		with self.assertRaises(ValueError):
			InternalStateProvider.getVariable("")
	def test_givenKeyNotPresent_raisesKeyError(self):
		with self.assertRaises(KeyError):
			InternalStateProvider.getVariable("key")
	def test_givenKeyPresent_returnsValue(self):
		InternalStateProvider.internalVariables["key"] = Object("15", "int")
		result = InternalStateProvider.getVariable("key")
		self.assertEqual(result.value, "15")
	def test_givenKeyPresent_returnsType(self):
		InternalStateProvider.internalVariables["key"] = Object("15", "int")
		result = InternalStateProvider.getVariable("key")
		self.assertEqual(result.type, "int")

class TestInternalStateProvider_clearState(unittest.TestCase):
	def test_removesVariablesFromInternalState(self):
		InternalStateProvider.internalVariables["key"] = Object("15", "int")
		InternalStateProvider.clearState()		
		self.assertEqual(len(InternalStateProvider.internalVariables), 0)


if __name__ == '__main__':
	unittest.main()