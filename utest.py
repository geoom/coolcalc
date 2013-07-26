import unittest
import calculator

class TestCoolCalculator(unittest.TestCase):

	def setUp(self):
		self.calc = calculator.Calculator()

	def tearDown(self):
		pass

	def test_add_2_to_2_retrieve_4(self):
		self.assertEquals(4, self.calc.add(2, 2))

	def test_add_5_to_7_retrieve_12(self):
		self.assertEquals(12, self.calc.add(5, 7))

	def test_commutative_property_is_met(self):
		self.assertEquals(self.calc.add(6, 2), self.calc.add(2, 6))

	def test_subtract_3_to_5(self):
		self.assertEquals(2, self.calc.subtract(5, 3))

	def test_subtract_3_to_2(self):
		self.assertEquals(-1, self.calc.subtract(2, 3))

	def test_commutative_property_isnt_met(self):
		self.assertNotEquals(self.calc.subtract(3, 1), self.calc.subtract(1, 3))

if __name__ == "__main__":
	unittest.main()