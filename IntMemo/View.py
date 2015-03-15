# coding=utf-8
import sys
import os

from Parser import parser
from Render import Renderer

flat_views = []
memo_views = []

class MetaFlatView(type):
    def __init__(cls, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, MetaFlatView)]
        if parents:
            flat_views.append(cls())

class MetaMemoView(type):
    def __init__(cls, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, MetaMemoView)]
        if parents:
            memo_views.append(cls())

class FlatView(object):
    __metaclass__ = MetaFlatView
    def __init__(self):
        self.content = ''

    def process(self):
        with open(self.path) as f:
            doc = f.read()
            renderer = Renderer('Markdown')
            self.content = renderer.render(doc)

class MemoView(object):
    __metaclass__ = MetaMemoView
    def __init__(self):
        self.content = []

    def process(self):
        if not os.path.exists(self.path):
            logging.fatal(
                    "The path (%s) of the Memo View is not exist" 
                    % self.path)
            return
        renderer = Renderer('Memo')
        for memo in os.listdir(self.path):
            path = os.path.join(self.path, memo)
            with open(path) as f:
                doc = f.read()
            self.content.append(
                    renderer.render(doc, path))



