import string 

class ExpresionAnalyser:

	def __is_number__(self, character):
		try:
			string.atoi(character)
			return True
		except ValueError:
			return False

	def parse(self, expresion):
		operatings = []
		operators = []
		tokens = string.split(expresion)
		for token in tokens:
			if self.__is_number__(token):
				operatings.append(string.atoi(token))
			else:
				operators.append(token)
		return {'operatings': operatings, 'operators': operators}