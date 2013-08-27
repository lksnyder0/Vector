class Vector:
	def __init__(self, v):
		self.__name__ = "Vector"
		if type(v) is list:
			self.__v = v
		else:
			raise VectorError("Not a valid Vector")
	def __add__(self, u):
		if type(u) is list:
			if len(u) == len(self.__v):
				return Vector([u[i] + self.__v[i] for i in range(len(self.__v))])
			else:
				raise VectorError("Vectors are not in the same Rn space")
		elif hasattr(u, "__name__") and u.__name__ == "Vector":
			if len(u) == len(self):
				return Vector([u.__v[i] + self.__v[i] for i in range(len(self.__v))])
		else:
			raise VectorError("Not a valid Vector")
	def __mul__(self, n):
		if type(n) is int or type(n) is float:
			return Vector([i*n for i in self.__v])
	def __repr__(self):
		s = ""
		l = 0
		for i in self.__v:  ## Finds the longest number
			if len(str(i)) > l:
				l = len(str(i))
		for i in self.__v:  ## Prints the vector in a netish fashion
			s += "|%s|\n" % (str(i).center(l+2))
		return s
	def __len__(self):
		return len(self.__v)


class VectorError(Exception):
	def __init__(self, error):
		self.value = error
	def __str__(self):
		print repr(self.value)

if __name__ == "__main__":
	v = Vector([1,1])
	print "Vector V:"
	print v
	print "v = v + [1,1]"
	v += [1,1]
	print v
	u = Vector([2,2])
	print "Vector u"
	print u
	print "v + u"
	print v + u
	print "3v"
	print v * 3
	## These should error.
	#v + 1