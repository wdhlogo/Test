#-*-coding:utf-8-*-
import csv

def getcsv(file_name='e:/tts.csv'):
	rows=[]
	with open(file_name,'rb') as f:
		readers=csv.reader(f,delimiter=',', quotechar='|')
		next(readers,None)
		for  row in readers:
			rows.append(row)
		return rows
		
def writecsv(file_name='e:/tts.csv'):
	with open(file_name,'wb') as f:
		write=csv.writer(f)
		write.writerow(['element','system'])
		data=[('selenium','webdriver'),('applium','android'),('abc','def')]
		write.writerows(data)
		f.close()


if __name__=='__main__':
	writecsv()
	getcsv()
