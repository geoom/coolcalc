import calculator

class CoolCalculator():

	def __init__(self, parser, validator):
		self.calc = calculator.Calculator()
		self.parser = parser
		self.validator = validator

	def __operate__(self, arithmetic_expression):
		i = None
		temp_result = 0
		if '*' in arithmetic_expression['operators']:
			i = arithmetic_expression['operators'].index('*')
			temp_result = self.calc.multiply(arithmetic_expression['operatings'][i],
											arithmetic_expression['operatings'][i+1])
		elif '/' in arithmetic_expression['operators']:
			i = arithmetic_expression['operators'].index('/')
			temp_result = self.calc.divide(arithmetic_expression['operatings'][i],
											arithmetic_expression['operatings'][i+1])
		elif '-' in arithmetic_expression['operators']:
			i = arithmetic_expression['operators'].index('-')
			temp_result = self.calc.subtract(arithmetic_expression['operatings'][i],
											arithmetic_expression['operatings'][i+1])
		elif '+' in arithmetic_expression['operators']:
			i = arithmetic_expression['operators'].index('+')
			temp_result = self.calc.add(arithmetic_expression['operatings'][i],
											arithmetic_expression['operatings'][i+1])
		else:
			# For this moment it's an error
			# we force the error to avoid problems
			assert False
		return (i, temp_result)

	def __simplify__(self, arithmetic_expression):
		
		if arithmetic_expression['operators'] == []:
			return arithmetic_expression

		(i, temp_result) = self.__operate__(arithmetic_expression) 
		simplify_expression = arithmetic_expression
		simplify_expression['operators'].pop(i)
		simplify_expression['operatings'].pop(i)
		simplify_expression['operatings'].pop(i)
		simplify_expression['operatings'].insert(i, temp_result)

		return self.__simplify__(simplify_expression)

	def calculate(self, arithmetic_expression):
		if not self.validator.validate(arithmetic_expression):
			raise SyntaxError("The expression is not valid")
		return str(self.__simplify__(self.parser.parse(arithmetic_expression))['operatings'][0])