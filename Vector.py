class Vector:
	def __init__(self, v):
		self.__name__ = "Vector"
		if type(v) is list:
			self.__v = v
		else:
			raise VectorError("Not a valid Vector")
	def __add__(self, u):
		if type(u) is list:
			if len(u) == len(self):
				return Vector([u[i] + self.getVector()[i] for i in range(len(self))])
			else:
				raise VectorError("Vectors are not in the same Rn space")
		elif hasattr(u, "__name__") and u.__name__ == "Vector":
			if len(u) == len(self):
				return Vector([u.getVector()[i] + self.getVector()[i] for i in range(len(self))])
		else:
			raise VectorError("Not a valid Vector")
	def __radd__(self, u):
		return self.__add__(u)
	def __sub__(self, u):
		if type(u) is list:
			if len(u) == len(self):
				return Vector([self.getVector()[i]-u[i] for i in range(len(self))])
			else:
				raise VectorError("Vectors are not in the same Rn space")
		elif hasattr(u, "__name__") and u.__name__ == "Vector":
			if len(u) == len(self):
				return Vector([self.getVector()[i] - u.getVector()[i] for i in range(len(self))])
	def __rsub__(self, u):
		if type(u) is list:
			if len(u) == len(self):
				return Vector([u[i] - self.getVector()[i] for i in range(len(self))])
			else:
				raise VectorError("Vectors are not in the same Rn space")
		else:
			raise VectorError("Not a valid vector")
	def __mul__(self, n):
		if type(n) is int or type(n) is float:
			return Vector([i*n for i in self.__v])
	def __rmul__(self, n):
		return self.__mul__(n)
	def __eq__(self, u):
		if type(u) is list:
			if len(u) == len(self):
				for i in range(len(self)):
					if u[i] != self.getVector()[i]:
						return False
				return True
			else:
				raise VectorError("Vectors are not in the same Rn space")
		elif hasattr(u, "__name__") and u.__name__ == "Vector":
			if len(u) == len(self):
				for i in range(len(self)):
					if u.getVector()[i] != self.getVector()[i]:
						return False
				return True
			else:
				raise VectorError("Vectors are not in the same Rn space")
		else:
			raise VectorError("Not a valid vector")
	def __ne__(self, u):
		if type(u) is list:
			if len(u) == len(self):
				for i in range(len(self)):
					if u[i] != self.getVector()[i]:
						return True
				return False
			else:
				raise VectorError("Vectors are not in the same Rn space")
		elif hasattr(u, "__name__") and u.__name__ == "Vector":
			if len(u) == len(self):
				for i in range(len(self)):
					if u.getVector()[i] != self.getVector()[i]:
						return True
				return False
			else:
				raise VectorError("Vectors are not in the same Rn space")
		else:
			raise VectorError("Not a valid vector")
	def __repr__(self):
		s = ""
		l = 0
		for i in self.__v:  ## Finds the longest number
			if len(str(i)) > l:
				l = len(str(i))
		for i in self.__v:  ## Prints the vector in a neatish fashion
			s += "|%s|\n" % (str(i).center(l+2))
		return s
	def __len__(self):
		return len(self.__v)
	def getVector(self):
		"""Returns the vector as a list"""
		return self.__v


class VectorError(Exception):
	def __init__(self, error):
		self.value = error
	def __str__(self):
		print repr(self.value)


if __name__ == "__main__":
	## Setting up Vectors
	v = Vector([1,1])
	print "Vector v:"
	print v
	u = Vector([2,2])
	print "Vector u:"
	print u

	## checking equality
	print "v == [1,1]:",
	if v == [1,1]: print "PASS"
	else: 
		print "FAIL"
		exit()
	print "Vector([1,1]) == Vector([1,1]):",
	if Vector([1,1]) == Vector([1,1]): print "PASS"
	else: print "FAIL"
	print

	## Adding a list to a Vector and assigning a variable
	print "v = v + [2,2] = [3,3]:",
	v += [2,2]
	if v == [3,3]:
		print "PASS"
		print "\nVector v is now:"
		print v
	else: print "FAIL"

	## Adding a vector to a list
	print "[12,12] + u:",
	if [12,12] + u == [14,14]: print "PASS"
	else: print "FAIL"

	## Adding two vectors
	print "v + u:",
	if v + u == [5,5]: print "PASS"
	else: print "FAIL"

	## Subtracting two vectors
	print "v - u:",
	if v - u == [1,1]: print "PASS"
	else: print "FAIL"

	## Subtracting vectors in a different order
	print "u - v:",
	if u - v == [-1, -1]: print "PASS"
	else: print "FAIL"

	## Subtracting a list from a vector
	print "v - [1,1]:",
	if v - [1,1] == [2,2]: print "PASS"
	else: print "FAIL"

	## Subtracting a vector from a list
	print "[1,1] - v:",
	if [1,1] - v == [-2, -2]: print "PASS"
	else: print "FAIL"

	## Multiplying a vector by an int
	print "v * 3:",
	if v * 3 == [9,9]: print "PASS"
	else: print "FAIL"

	## Multiplying vectors by an int and then adding the results
	print "2u + 4v:",
	if 2*u + 4*v == [16, 16]: print "PASS"
	else: print "FAIL"
	
	## These should error.
	#v + 1