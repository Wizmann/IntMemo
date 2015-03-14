# coding=utf-8
import sys
import os

from Parser import parser

flat_views = []
memo_views = []

class MetaView(object):
    views = []
    def __init__(cls, name, bases, attrs):
        parents = [b for b in bases if isinstance(b, MetaPattern))]
        if parents:
            views.append(cls())

class MetaFlatView(MetaView):
    views = flag_views

class MetaMemoView(MetaView):
    views = memo_views

class BaseView(object):
    def process(self):
        raise NotImplementedError

class BaseFlatView(BaseView):
    __metaclass__ = MetaFlatView

class BaseMemoView(BaseView):
    __metaclass__ = MetaMemoView

class FlatView(BaseFlatView):
    def __init__(self):
        self.content = ''

    def process(self):
        with open(self.path) as f:
            doc = f.read()
            renderer = Renderer('Markdown')
            self.content = renderer.render(doc)

class MemoView(self):
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
            with open(memo) as f:
                doc = f.read()
            self.content.append(
                    renderer.render(doc))



