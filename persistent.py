
class ExpressionStorageManager():

	def __init__(self, handler):
		self.handler = handler

	def insert(self, expression, result):
		line_in_file = expression + ';' + result
		self.handler.save(line_in_file)
