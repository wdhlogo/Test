#-*-coding:utf-8-*-
#csv combine ddt
from selenium import webdirver
from ddt import ddt,data,unpack
import usecsv
import unittest,sys

reload(sys)
sys.setdefaultencoding('utf-8')
@ddt

class Testbaidu(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.FireFox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')
		@data(*usecsv.getcsv("e:\\tts.csv"))
		@unpack

	
	def testcase_01(self,actual,expect):
		self.driver.find_element_by_id('kw'.sendkeys(actual)
		import time
		time.sleep(5)


	def tearDown(self):
		self.driver.quit()
	

if__name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(Testbaidu)
	unittest.TextTestRunner(verbosity=2).run(suite)

