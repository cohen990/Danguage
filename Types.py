class Object:
	def __init__(self, value, objectType, operators = {}):
		self.value = value
		self.type = objectType
		self.operators = operators

	def __str__(self):
		return str(self.value) + " <" + self.type + ">"
	def __repr__(self):
		return self.__str__()

	def CheckType(obj1, obj2, requiredType, operator):
		if not type(obj2) is requiredType:
			raise TypeError(
				"Cannot perform <" + str(type(obj1)) + "> " + operator + 
				" <" + str(type(obj2)) + ">")

class DInt(Object):
	def __init__(self, value):
		value = int(value)
		operators = DInt.GetOperators(value)
		Object.__init__(
			self,
			value = value,
			objectType = "int",
			operators = operators)
	
	def GetOperators(value):
		return {
			"+": DInt.Add(value),
			"-": DInt.Subtract(value),
			"*": DInt.Multiply(value),
			"/": DInt.Divide(value)}

	def Add(value):
		def func(num):
			Object.CheckType(value, num, int, "+")

			return value + num
		return func

	def Subtract(value):
		def func(num):
			Object.CheckType(value, num, int, "-")

			return value - num
		return func

	def Multiply(value):
		def func(num):
			Object.CheckType(value, num, int, "*")
			
			return value * num
		return func

	def Divide(value):
		def func(num):
			Object.CheckType(value, num, int, "/")

			return int(value / num)
		return func

class DString(Object):
	def __init__(self, value):
		if value == None: raise TypeError("value must not be None")
		value = str(value)
		if value.startswith("\"") and value.endswith("\""): value = value[1:-1]
		operators = DString.GetOperators(value)
		Object.__init__(
			self,
			value = value,
			objectType = "string",
			operators = operators)
	
	def GetOperators(value):
		return {"+": DString.Add(value)}

	def Add(value):
		def func(string):
			Object.CheckType(value, string, str, "+")
			if string.startswith("\"") and string.endswith("\""): string = string[1:-1]

			return "\"" + value + string + "\""
		return func
