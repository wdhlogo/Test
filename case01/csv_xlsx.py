#-*-coding:utf-8-*-
import csv,xlrd
from selenium import webdriver
import time as t

def getcsv(value1,value2,file_name='E://tts.csv'):
	rows=[]
	with open(file_name,'rb') as f:
		readers=csv.reader(f,delimiter=',', quotechar='|')
		next(readers,None)
		for  row in readers:
			rows.append(row)
		print  rows[value1][value2]
		return rows[value1][value2]

def writecsv(file_name):
	with open(file_name,'wb') as f:
		write=csv.writer(f)
		write.writerow(['element','system'])
		data=[('selenium','webdriver'),('applium','android'),('abc','def')]
		write.writerows(data)
		f.close()

def getexcel(rowvalue,colvalue,sheetname='Sheet1',file_name='E:\\tts.xlsx'):
	book=xlrd.open_workbook(file_name)
	sheet=book.sheet_by_name(sheetname)
	#print sheet.cell_value(0,0)
	#print sheet.cell_value(rowvalue,colvalue)
	return sheet.cell_value(rowvalue,colvalue)

def teststfr(driver,value9):
	frpath=driver.find_element_by_xpath(value9)
	driver.switch_to_frame(frpath)
	t.sleep(1)

def testpic(driver):
	t.sleep(2)
	nowTime=t.strftime("%Y%m%d.%H.%M.%S")
	driver.get_screenshot_as_file('E:\\DHtest\\image\\%s.png'%nowTime)
	t.sleep(2)
	
	
def clicklogin(driver,username,password,xppath1,xppath2):
	#print "1111"
	t.sleep(3)
	name=driver.find_element_by_xpath(xppath1)
	name.click()
	name.clear()
	print username
	name.send_keys(username)
	t.sleep(2)
	print "2222"
	passwd=driver.find_element_by_xpath(xppath2)
	passwd.click()
	passwd.clear()
	print password
	passwd.send_keys(password)
	t.sleep(2)

def clickbutton(driver,xppath):
	return driver.find_element_by_xpath(xppath)
	t.sleep(2)

def get_text(driver,ppath):
	return driver.find_element_by_xpath(ppath).text

"""
if __name__=='__main__':
	getexcel(0,0,'Sheet1','e:\\tts.xlsx')
	getcsv(0,0)
"""