
class FileHandler():

	file_name = "cool_calculator.txt"

	def save(self, text_to_save):
		f = open(self.file_name, 'a')
		f.write(text_to_save + '\n')
		f.close()
