from Object import *

class InternalStateProvider:
	internalVariables = {}
	knownTypes = ["int", "string"]
	__defaultKnownTypes = ["int", "string"]
	operators = ["+"]
	__defaultOperators = ["+"]
	def getVariable(key):
		if not key: raise ValueError("key cannot be empty")
		return InternalStateProvider.internalVariables[key]
	def setVariable(key, value, objectType):
		InternalStateProvider.internalVariables[key] = Object(value, objectType)
	def tryLookup(key):
		if not key: raise ValueError("key cannot be empty")
		if key in InternalStateProvider.internalVariables:
			return InternalStateProvider.getVariable(key)
		return key
	def clearState():
		InternalStateProvider.internalVariables = {}
		InternalStateProvider.knownTypes = InternalStateProvider.__defaultKnownTypes
		InternalStateProvider.operators = InternalStateProvider.__defaultOperators	