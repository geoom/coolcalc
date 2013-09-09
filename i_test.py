import unittest
import os
from handler import FileHandler, DatabaseHandler
from storage import ExpressionStorageManagerToFile
from model import Operation

class TestFileSystemStorageManager(unittest.TestCase):

	def test_the_expression_is_saved_on_sytem_file(self):

		found = False
		handler = FileHandler()
		exp_storage = ExpressionStorageManagerToFile(handler)

		exp_storage.insert("2 + 7", "9")

		if not os.path.isfile(handler.file_name):
			self.fail("file was not created")

		exp_file = open(handler.file_name)
		for line in exp_file:
			if line == "2 + 7;9\n":
				found = True

		self.assertTrue(found)
		os.remove(handler.file_name)

class TestDatabaseStorageManager(unittest.TestCase):

	def test_the_expression_is_saved_on_database(self):

		handler = DatabaseHandler()
		handler.execute("TRUNCATE operations")

		new_operation = Operation()
		new_operation.id = 21
		new_operation.expression = "1 * 3 - 6 + 4"
		new_operation.result = "1"
		new_operation.save()

		obtained_operation = Operation.get(new_operation.id)
		self.assertEquals("1 * 3 - 6 + 4", obtained_operation[1])
		self.assertEquals("1", obtained_operation[2])

		handler.execute("TRUNCATE operations")


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestFileSystemStorageManager))
	suite.addTest(unittest.makeSuite(TestDatabaseStorageManager))
	unittest.TextTestRunner(verbosity=3).run(suite)