from Object import *

class InternalStateProvider:
	internalVariables = {}
	knownTypes = ["int", "string"]
	operators = ["+"]
	def getVariable(key):
		return
	def setVariable(key, value, objectType):
		InternalStateProvider.internalVariables[key] = Object(value, objectType)