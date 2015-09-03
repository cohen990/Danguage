from Types import *

class InternalStateProvider:
	def __init__(self):
		self.clearState()

	__defaultKnownTypes = ["int", "string"]
	__defaultOperators = ["+", "-", "*", "/"]

	def getVariable(self, key):
		if not key: raise ValueError("key cannot be empty")
		return self.internalVariables[key]
	def setVariable(self, key, value):
		self.internalVariables[key] = value
	def tryLookup(self, key):
		if not key: raise ValueError("key cannot be empty")
		if key in self.internalVariables:
			return self.getVariable(key)
		return key
	def clearState(self):
		self.internalVariables = {}
		self.knownTypes = InternalStateProvider.__defaultKnownTypes
		self.operators = InternalStateProvider.__defaultOperators	