#-*-coding:utf-8-*-
import unittest
import os
import HTMLTestRunner

case_path="E:\\DHtest\\case01"

report_path="E:\\DHtest\\report01\\result.html"

def all_case():
	
	discover=unittest.defaultTestLoader.discover(case_path,pattern="location_excel.py",top_level_dir=None)
	return discover


if __name__ == '__main__':
	#report_abspath=os.path.join(report_path,"result.html")

	fp=open(report_path,'wb')
	
	runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='the result is as below:',description='situation for cases:')
	
	runner.run(all_case())
	fp.close()