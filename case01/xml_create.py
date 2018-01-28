#-*-coding:utf-8-*-
from xml.dom  import minidom

def create_xml_test(filename):
	xml=minidom.Document()
	root=xml.createElement('root')
	root.setAttribute('xmlns:xsi"http://www.baidu.com','12')
	xml.appendChild(root)
	text_node=xml.createElement('element')
	text_node.setAttribute('id','id 1')
	root.appendChild(text_node)
	text=xml.createTextNode('hello world')
	text_node.appendChild(text)
	tag=xml.createElement('tag')
	tag.setAttribute('data','tag data')
	text_node.appendChild(tag)
	f=open(filename,'w')
	f.write(xml.toprettyxml(encoding='utf-8'))
	f.close()
if __name__=='__main__':
	create_xml_test('1.xml')