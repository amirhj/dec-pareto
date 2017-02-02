import math

class Functions:
	def __init__(self, fg):
		self.fg = fg

	def calculate(self, name, values):
		function = getattr(self, name)
		return function(values)

	def f1(self, values):
		v0 = values["v0"]
		v1 = values["v1"]
		v3 = values["v3"]
		n = self.fg.constants["n"]

		value = (1-math.exp(-1*sum((v-1/math.sqrt(n))**2 for v in [v0, v1, v3])))*15 + 1
		
		return value

	def f2(self, values):
		v1 = values["v1"]
		v2 = values["v2"]
		v4 = values["v4"]
		n = self.fg.constants["n"]

		value = (1-math.exp(-1*sum((v+1/math.sqrt(n))**2 for v in [v1, v2, v4])))*1 + 0.2

		return value

	def f3(self, values):
		v3 = values["v3"]
		v4 = values["v4"]
		v5 = values["v5"]
		n = self.fg.constants["n"]

		value = (1-math.exp(-1*sum((v-2/math.sqrt(n))**2 for v in [v3, v4, v5])))*1 + 0.8

		return value