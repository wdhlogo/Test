#-*-coding:utf-8-*-

from xml.dom import minidom

def read_xml_test(filename):
	xml=minidom.parse(filename)
	root=xml.documentElement
	elements=root.getElementByTagName('element')

	for element in elements:

		if element.hasAttribute('id'):
			print 'id:',element.getAttribute('id')

		for node in element.childNodes:

			if node.nodeName=='#text':
				text=node.data.replace('\n','')
				#print u'\text1:',text
				print text

			else:
				print '\t'+node.nodeName
				for attr,attr_val in node.attributes.items():
					print '\t\t',attr,':',attr_val


	
if __name__=='__main__':
	read_xml_test('e:\\1.xml')
	raw_input('ok')
