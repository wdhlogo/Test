##-*-coding:utf-8-*-
import unittest
import os

#����·��
case_path=os.path.join(os.getcwd(),"case01")
print case_path

#������·��
report_path=os.path.join(os.getcwd(),"report")
print report_path


discover=unittest.defaultTestLoader.discover(case.path)
print discover
