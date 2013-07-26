import unittest
import calculator
import analyzer

class TestCalculator(unittest.TestCase):

	def setUp(self):
		self.calc = calculator.Calculator()

	def tearDown(self):
		pass

	def test_add_2_to_2_retrieve_4(self):
		self.assertEquals(4, self.calc.add(2, 2))

	def test_add_5_to_7_retrieve_12(self):
		self.assertEquals(12, self.calc.add(5, 7))

	def test_commutative_property_is_met(self):
		self.assertEquals(self.calc.add(6, 2), 
						  self.calc.add(2, 6))

	def test_subtract_3_to_5(self):
		self.assertEquals(2, self.calc.subtract(5, 3))

	def test_subtract_3_to_2(self):
		self.assertEquals(-1, self.calc.subtract(2, 3))

	def test_commutative_property_isnt_met(self):
		self.assertNotEquals(self.calc.subtract(3, 1), 
							 self.calc.subtract(1, 3))

	def test_add_2_negative_numbers(self):
		self.assertEquals(0, self.calc.add(-2, 2))

	def test_subtract_2_negative_numbers(self):
		self.assertEquals(-7, self.calc.subtract(-5, 2))
		self.assertEquals(-5, self.calc.subtract(-7, -2))

	def test_exact_division(self): 
		self.assertEquals(1, self.calc.divide(2, 2))
		self.assertEquals(2, self.calc.divide(10, 5))

	def test_negative_exact_division(self):
		self.assertEquals(-2, self.calc.divide(10, -5))
		self.assertEquals(2, self.calc.divide(-10, -5))

	def test_no_exact_division_throws_exception(self):
		self.assertRaises(ValueError, self.calc.divide, 3, 2)

	def test_division_by_0_throws_exception(self):
		self.assertRaises(ZeroDivisionError, self.calc.divide, 3, 0)

class TestAnalyzer(unittest.TestCase):

	def setUp(self):
		self.expAnalyzer = analyzer.ExpresionAnalyser()

	def tearDown(self):
		pass

	def test_fetch_operatings_and_operators_when_add_2_to_2(self):
		self.assertEquals({'operatings': [2, 2], 
							'operators': ['+']}, 
							self.expAnalyzer.parse("2 + 2"))

	def test_fetch_operatings_and_operators_when_divide_10_by_negative_5(self):
		self.assertEquals({'operatings': [10, -5], 
							'operators': ['/']}, 
							self.expAnalyzer.parse("10 / -5"))

	def test_fetch_operatings_and_operators_of_complex_expresion_without_parenthesis(self):
		self.assertEquals({'operatings': [5, 4, 2, 2], 
							'operators': ['+', '*', '/']}, 
							self.expAnalyzer.parse("5 + 4 * 2 / 2"))


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestCalculator))
	suite.addTest(unittest.makeSuite(TestAnalyzer))
	unittest.TextTestRunner(verbosity=3).run(suite)