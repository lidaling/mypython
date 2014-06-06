__author__ = 'lidl'
#http://www.besttome.com/html/python_read_xml_file.html
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

file='/Users/lidl/test.xml'
tree = ET.parse(file)
for item in tree.findall('Item'):
    subcontent=item.find('type').text
    if(subcontent=='feature'):
        print(subcontent)
        xitem=item.find('x')
        xitem.text='10000'

tree.write(file,'UTF-8')
