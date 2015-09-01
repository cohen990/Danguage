class Object:
	def __init__(self, value, objectType):
		self.value = value
		self.type = objectType
	def __str__(self):
		return self.value + " <" + self.type + ">"
	def __unicode__(self):
		return u(self.__str__())
	def __repr__(self):
		return self.__str__()