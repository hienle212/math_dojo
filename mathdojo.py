
from flask import Flask 
app = Flask(__name__)
# Part 1
class MathDojo(object):
	def __init__(self):
		self.result = 0

	def add(self, *num):
		for i in num:
			self.result += i
		return self
	def subtract(self, *num):
		for i in num:
			self.result -= i
		return self
	def result(self):
		return result

# md = MathDojo()
print MathDojo().add(2).add(2,5).subtract(3,2).result

#Part2 & 3
class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *num):
		for i in num:
			if type(i) == type(list()):
				for j in i:
					self.result += j
			elif type(i) == type(tuple()):
				for k in i:
					self.result += i
			else :
				self.result += i
		return self 
	def subtract(self, *num):
		for i in num:
			if type(i) == type(list()):
				for j in i:
					self.result -= j
			elif type(i) == type(tuple()):
				for k in i:
					self.result -= i
			else :
				self.result -= i

		return self
	def result(self):
		return result

print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
