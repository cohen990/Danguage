class BaseObject(object):
	def __init__(self):
		self.properties = []
		self.functions = []
		self.type = "BaseObject"
		self.value = None

	def addFunction(self, dFunction):
		if not isinstance(dFunction, DFunction):
			raise TypeError("dFunction must be a DFunction")
		self.functions.append(dFunction)
	def addProperty(self, dProperty):
		if not isinstance(dProperty, DProperty): 
			raise TypeError("dProperty cannot be None")
		self.properties.append(dProperty)

class DFunction:
	def __init__(self, name, arguments, returnType):
		self.name = name
		self.arguments = arguments
		self.returnType = returnType

class DProperty:
	def __init__(self, name, dType):
		self.name = name
		self.type = dType

class DInt(BaseObject):
	def __init__(self):
		self.properties = [] 
		self.functions = DInt.getIntFunctions()
		self.type="int"

	def getIntFunctions():
		plus = DFunction("+", ["int"], "int")
		return [plus]