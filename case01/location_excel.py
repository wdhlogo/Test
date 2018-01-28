#-*-coding:utf-8-*-
from selenium import webdriver
import usecsv
import csv_xlsx
import unittest

class Testbaidu(unittest.TestCase):

	def setUp(self):
		self.driver=webdriver.Ie()
		self.driver.maximize_window()
		self.driver.implicitly_wait(100)
		self.driver.get('https://mail.126.com/')
		
		
	# ‰»Î’À∫≈√‹¬Î
	def testcase_01(self):
		driver=self.driver
		#print csv_xlsx.getexcel(0,0)
		csv_xlsx.clickbutton(driver,'//*[@id="lbNormal"]').click()	
		csv_xlsx.teststfr(driver,'//*[@id="x-URS-iframe"]')
		#print "111"
		csv_xlsx.clicklogin(driver,csv_xlsx.getexcel(0,0),csv_xlsx.getexcel(0,1),'//*[@id="account-box"]/div[2]/input','//*[@id="login-form"]/div/div[3]/div[2]/input[2]')
		csv_xlsx.clickbutton(driver,'//*[@id="dologin"]').click()
		#//div[@id="cnt-box"]/div[2]/from/div/div[8]/a
		driver.switch_to_default_content()
		self.driver.implicitly_wait(80)
		self.assertEqual(csv_xlsx.get_text(driver,'//*[@id="dvContainer"]/div/div/div/div/div[2]/span/span'),csv_xlsx.getexcel(0,2))
		csv_xlsx.testpic(driver)
	
	# ‰»Î’À∫≈√ª”–√‹¬Î
	def testcase_02(self):
		driver=self.driver
		csv_xlsx.clickbutton(driver,'//*[@id="lbNormal"]').click()	
		csv_xlsx.teststfr(driver,'//*[@id="x-URS-iframe"]')
		csv_xlsx.clicklogin(driver,csv_xlsx.getexcel(1,0),csv_xlsx.getexcel(1,1),'//*[@id="account-box"]/div[2]/input','//*[@id="login-form"]/div/div[3]/div[2]/input[2]')
		csv_xlsx.clickbutton(driver,'//*[@id="dologin"]').click()
		driver.switch_to_default_content()
		csv_xlsx.testpic(driver)
		
				
	# ‰»Î√‹¬Î√ª”–’À∫≈
	def testcase_03(self):
		driver=self.driver
		csv_xlsx.clickbutton(driver,'//*[@id="lbNormal"]').click()
		csv_xlsx.teststfr(driver,'//*[@id="x-URS-iframe"]')
		csv_xlsx.clicklogin(driver,csv_xlsx.getexcel(2,0),csv_xlsx.getexcel(2,1),'//*[@id="account-box"]/div[2]/input','//*[@id="login-form"]/div/div[3]/div[2]/input[2]')
		csv_xlsx.clickbutton(driver,'//*[@id="dologin"]').click()
		driver.switch_to_default_content()
		csv_xlsx.testpic(driver)
		
		
	def tearDown(self):
		self.driver.quit()
	
"""
if __name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(Testbaidu)
	unittest.TextTestRunner(verbosity=2).run(suite)

"""