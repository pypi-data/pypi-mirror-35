from lxml import etree

def parse_xml_string(xmlstring):
    return etree.fromstring(xmlstring)