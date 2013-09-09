# -*- coding: utf-8 *-*
import MySQLdb
import sys

class FileHandler():

	file_name = "cool_calculator.txt"

	def save(self, text_to_save):
		f = open(self.file_name, 'a')
		f.write(text_to_save + '\n')
		f.close()

class DatabaseHandler:

    def __init__(self, db_host='localhost', db_user='root', db_pass='root',
                 db_name='coolcalculator'):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name

    def execute(self, query, values=''):

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.db_user,
                                  passwd=self.db_pass, db=self.db_name)

            cursor = conn.cursor()
            
            if values != '':
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            conn.commit()
            cursor.close()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
        finally:    
            if conn:    
                conn.close()

    def get_one_result(self, query, values):

        try:
            conn = MySQLdb.connect(host=self.db_host, user=self.db_user,
                                  passwd=self.db_pass, db=self.db_name)

            cursor = conn.cursor()
            cursor.execute(query, values)
            result = cursor.fetchone()

            cursor.close()
            
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
        finally:    
            if conn:    
                conn.close()

        return result