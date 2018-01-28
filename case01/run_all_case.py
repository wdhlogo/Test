##-*-coding:utf-8-*-
import unittest
import os

#用例路径
case_path=os.path.join(os.getcwd(),"case01")
print case_path

#报告存放路径
report_path=os.path.join(os.getcwd(),"report")
print report_path


discover=unittest.defaultTestLoader.discover(case.path)
print discover
