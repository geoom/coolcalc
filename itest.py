import unittest
import os
from hanlder import FileHandler
from persistent import ExpressionStorageManager

class TestExpressionStorageManager(unittest.TestCase):

	def test_the_expression_is_saved_on_sytem_file(self):

		found = False
		handler = FileHandler()
		exp_storage = ExpressionStorageManager(handler)

		exp_storage.insert("2 + 7", "9")

		if not os.path.isfile(handler.file_name):
			self.fail("file was not created")

		exp_file = open(handler.file_name)
		for line in exp_file:
			if line == "2 + 7;9\n":
				found = True

		self.assertTrue(found)
		os.remove(handler.file_name)


if __name__ == "__main__":
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(TestExpressionStorageManager))
	unittest.TextTestRunner(verbosity=3).run(suite)