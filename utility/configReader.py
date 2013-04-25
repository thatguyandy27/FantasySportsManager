# -*- coding: utf-8 *-*
import xml.etree.ElementTree as ET
from configuration import configuration


#after writing this class out it almost looks identical to using the
#actual ElementTree items.  Oh well good practice anyway.
class configReader:

    @staticmethod
    def readConfig(fileName):
        configTree = ET.parse(fileName)
        root = configTree.getroot()
        return configReader.__parseNode(root)

    @staticmethod
    def __parseNode(node):
        #print 'node.text', node.text
        #print 'node.tag', node.tag
        nodeObject = configuration(node.attrib, node.tag, node.text)

        for child in node:
            nodeObject.children.append(configReader.__parseNode(child))

        return nodeObject


if __name__ == '__main__':
    print configReader.readConfig('sampleConfig.xml')
