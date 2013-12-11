import re

class ValidatorArithmeticExpression():

	def validate(self, expression):
		if re.match("-*\d+( [-+*/] -*\d+)+$", expression):
			return True
		else:
			return False
