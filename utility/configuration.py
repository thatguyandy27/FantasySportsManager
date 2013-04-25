# -*- coding: utf-8 *-*


class configuration():

    def __init__(self, attributes, tag, text):
        self.attributes = attributes
        self.tag = tag
        self.text = text.strip()
        self.children = []

    def __repr__(self):
        outputString = '{{tag: {0.tag}, text: {0.text}, children:{0.children}}}'.format(self)
        return outputString
