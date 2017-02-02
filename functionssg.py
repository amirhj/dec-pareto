import math

class Functions:
	def __init__(self, fg):
		self.fg = fg

	def calculate(self, name, values):
		function = getattr(self, name)
		return function(values)

	def v18(self, values):
		g18 = values["g18"]
		t17 = values["t17"]
		value = g18 - 19 - t17
		return value**2

	def v18u(self, values):
		g18 = values["g18"]
		value = g18 * 0.350000
		return value

	def v19(self, values):
		g19 = values["g19"]
		t17 = values["t17"]
		t5 = values["t5"]
		value = g19 - 19 - t5 + t17
		return value**2

	def v19u(self, values):
		g19 = values["g19"]
		value = g19 * 0.500000
		return value

	def v12(self, values):
		g12 = values["g12"]
		t12 = values["t12"]
		t7 = values["t7"]
		value = g12 - 18 - t7 + t12
		return value**2

	def v12u(self, values):
		g12 = values["g12"]
		value = g12 * 0.200000
		return value

	def v13(self, values):
		g13 = values["g13"]
		t14 = values["t14"]
		t13 = values["t13"]
		t11 = values["t11"]
		value = g13 - 28 - t11 + t14 + t13
		return value**2

	def v13u(self, values):
		g13 = values["g13"]
		value = g13 * 0.200000
		return value

	def v10(self, values):
		g10 = values["g10"]
		t10 = values["t10"]
		value = g10 - 18 - t10
		return value**2

	def v10u(self, values):
		g10 = values["g10"]
		value = g10 * 0.350000
		return value

	def v11(self, values):
		g11 = values["g11"]
		t11 = values["t11"]
		t12 = values["t12"]
		value = g11 - 18 - t12 + t11
		return value**2

	def v11u(self, values):
		g11 = values["g11"]
		value = g11 * 0.400000
		return value

	def v16(self, values):
		g16 = values["g16"]
		t16 = values["t16"]
		t15 = values["t15"]
		value = g16 - 28 - t15 + t16
		return value**2

	def v16u(self, values):
		g16 = values["g16"]
		value = g16 * 0.350000
		return value

	def v17(self, values):
		g17 = values["g17"]
		t16 = values["t16"]
		value = g17 - 18 - t16
		return value**2

	def v17u(self, values):
		g17 = values["g17"]
		value = g17 * 0.500000
		return value

	def v14(self, values):
		g14 = values["g14"]
		t14 = values["t14"]
		value = g14 - 19 - t14
		return value**2

	def v14u(self, values):
		g14 = values["g14"]
		value = g14 * 0.200000
		return value

	def v15(self, values):
		g15 = values["g15"]
		t15 = values["t15"]
		t9 = values["t9"]
		value = g15 - 21 - t9 + t15
		return value**2

	def v15u(self, values):
		g15 = values["g15"]
		value = g15 * 0.700000
		return value

	def v0(self, values):
		g0 = values["g0"]
		t2 = values["t2"]
		t3 = values["t3"]
		t0 = values["t0"]
		t1 = values["t1"]
		value = g0 - 19 + t2 + t3 + t0 + t1
		return value**2

	def v0u(self, values):
		g0 = values["g0"]
		value = g0 * 0.700000
		return value

	def v1(self, values):
		g1 = values["g1"]
		t0 = values["t0"]
		value = g1 - 28 - t0
		return value**2

	def v1u(self, values):
		g1 = values["g1"]
		value = g1 * 0.350000
		return value

	def v2(self, values):
		g2 = values["g2"]
		t1 = values["t1"]
		value = g2 - 19 - t1
		return value**2

	def v2u(self, values):
		g2 = values["g2"]
		value = g2 * 0.350000
		return value

	def v3(self, values):
		g3 = values["g3"]
		t2 = values["t2"]
		value = g3 - 21 - t2
		return value**2

	def v3u(self, values):
		g3 = values["g3"]
		value = g3 * 0.500000
		return value

	def v4(self, values):
		g4 = values["g4"]
		t4 = values["t4"]
		t3 = values["t3"]
		value = g4 - 19 - t3 + t4
		return value**2

	def v4u(self, values):
		g4 = values["g4"]
		value = g4 * 0.350000
		return value

	def v5(self, values):
		g5 = values["g5"]
		t6 = values["t6"]
		t7 = values["t7"]
		t5 = values["t5"]
		t4 = values["t4"]
		value = g5 - 21 - t4 + t6 + t7 + t5
		return value**2

	def v5u(self, values):
		g5 = values["g5"]
		value = g5 * 0.700000
		return value

	def v6(self, values):
		g6 = values["g6"]
		t18 = values["t18"]
		t8 = values["t8"]
		value = g6 - 21 - t8 + t18
		return value**2

	def v6u(self, values):
		g6 = values["g6"]
		value = g6 * 0.400000
		return value

	def v7(self, values):
		g7 = values["g7"]
		t8 = values["t8"]
		t6 = values["t6"]
		value = g7 - 19 - t6 + t8
		return value**2

	def v7u(self, values):
		g7 = values["g7"]
		value = g7 * 0.500000
		return value

	def v8(self, values):
		g8 = values["g8"]
		t9 = values["t9"]
		t18 = values["t18"]
		value = g8 - 28 - t18 + t9
		return value**2

	def v8u(self, values):
		g8 = values["g8"]
		value = g8 * 0.200000
		return value

	def v9(self, values):
		g9 = values["g9"]
		t10 = values["t10"]
		t13 = values["t13"]
		value = g9 - 19 - t13 + t10
		return value**2

	def v9u(self, values):
		g9 = values["g9"]
		value = g9 * 0.200000
		return value