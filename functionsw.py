import math

class Functions:
	def __init__(self, fg):
		self.fg = fg

	def calculate(self, name, values):
		function = getattr(self, name)
		return function(values)

	def f1(self, values):
		x = values["x1"]
		a = -0.2
		b = 6
		c = -5

		value = a*x**2 + b*x + c
		
		return value

	def f2(self, values):
		x = values["x2"]
		a = -0.06
		b = 2.52
		c = 0

		value = a*x**2 + b*x + c
		
		return value

	def f3(self, values):
		x = values["x3"]
		a = -0.29
		b = 6.38
		c = -3

		value = a*x**2 + b*x + c
		
		return value

	def f4(self, values):
		x = values["x4"]
		a = -0.13
		b = 5.98
		c = -6

		value = a*x**2 + b*x + c
		
		return value

	def f5(self, values):
		x = values["x5"]
		a = -0.055
		b = 3.63
		c = -23

		value = a*x**2 + b*x + c
		
		return value

	def f6(self, values):
		x = values["x6"]
		a = -0.15
		b = 7.5
		c = -15

		value = a*x**2 + b*x + c
		
		return value

	def F1(self, values):
		x = values["x"]
		a = 0
		Q = 0

		value = a*x**2 + b*x + c
		
		return value