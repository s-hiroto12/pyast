import ast
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

source_file = 'sample.py'
output_file = 'ast.xml'

#generate ast
with open(source_file, 'r', encoding='utf-8') as file:
    source_code = file.read()
tree = ast.parse(source_code)

#convert ast　to xml
def ast_to_xml(node):
    element = ET.Element(node.__class__.__name__)
    for field, value in ast.iter_fields(node):
        if isinstance(value, ast.AST):
            child = ast_to_xml(value)
            child.attrib['field'] = field
            element.append(child)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    child = ast_to_xml(item)
                    child.attrib['field'] = field
                    element.append(child)
        else:
            child = ET.Element('Token')
            child.text = str(value)
            child.attrib['field'] = field
            element.append(child)
    return element

root = ast_to_xml(tree)

formatted_xml = minidom.parseString(ET.tostring(root)).toprettyxml(indent='  ')

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(formatted_xml)
