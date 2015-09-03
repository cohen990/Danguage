class BaseObject:
	def __init__(self):
		self.properties = []
		self.functions = []
	def addFunction(self, dFunction):
		if not isinstance(dFunction, DFunction):
			raise TypeError("dFunction cannot be None")
		self.functions.append(dFunction)
	def addProperty(self, dProperty):
		self.properties.append(dProperty)

class DFunction:
	def __init__(self, arguments, returnType):
		self.arguments = arguments
		self.returnType = returnType