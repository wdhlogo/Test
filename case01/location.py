#-*-coding:utf-8-*-
from selenium import webdriver
import usecsv
import unittest

class Testbaidu(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.FireFox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get(usecsv.getcsv(0,0))

	
	def testcase_01(self):
		self.driver.find_element_by_id('kw'.sendkeys(usecsv.getcsv(0,0)))
		import time
		time.sleep(5)


	def tearDown(self):
		self.driver.quit()
	

if__name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(Testbaidu)
	unittest.TextTestRunner(verbosity=2).run(suite)

