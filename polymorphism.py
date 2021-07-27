import math

class Shape:
	def calArea():
		return 0.0
	def calCircle():
		return 0.0

class Rect(Shape):
	def __init__(self,length,width):
		self.length = length
		self.width = width
	
	def calarea(self):
		return self.length * self.width

	def calCircle(self):
		return 2 * (self.length * self.width)

class Square(Rect):
	def __init__(self,length):
		super().__init__(length,length) 
		#相当于把两个length填进前面一个类的init的self后面两格