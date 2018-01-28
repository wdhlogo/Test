#-*-coding:utf-8-*-
import unittest
    
class IntegerArithmeticTestCase(unittest.TestCase):
	def setUp(self):
		print "start!"
	def tearDown(self):
		print  "end!"

	def test012(self):
		print "执行用例 03"
	def test001(self):
		print "execute case 01"
	def test013(self):
		print "execute case 02"
	def addtest(self):
		print "add方法"
	
	
if __name__ == '__main__':
	unittest.main()