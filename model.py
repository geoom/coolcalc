
from handler import DatabaseHandler

class Operation:

	handler = DatabaseHandler()

	def __init__(self):
		self.id = None
		self.expression = ''
		self.result = ''
		self.handler = DatabaseHandler()

	def __str__(self):
		return self.id + self.expression + self.result

	def save(self):
		"""Save a new operation on operations table"""
		query = "INSERT INTO operations (id, expression, result) VALUES (%s, %s, %s)"
		values = (self.id, self.expression, self.result)
		self.handler.execute(query, values)

	@classmethod
	def get(self, id):
		query = "SELECT id, expression, result FROM operations WHERE id = %s"
		values = (id)
		return self.handler.get_one_result(query, values)
