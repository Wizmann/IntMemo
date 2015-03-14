#coding=utf-8
import sys
import os
import json
import jinja2

class Generator(object):
    def __new__(cls, name):
        if name == 'FlatView':
            return FlatViewGenerator()
        elif name == 'MemoView':
            return MemoViewGenerator()

class BaseGenerator(object):
    def generate(self, view):
        raise NotImplementedError

class FlatViewGenerator(BaseGenerator):
    def generate(self, site, view):
        tpl = os.path.join(site.theme, 'flat_view.html')
        env = jinja2.Environment(
                loader = jinja2.FileSystemLoader(tpl),
                autoescape=True)
        with open(view.content['Path'], 'w') as f:
            f.write(tpl.render(site, view, doc))

class MemoViewGenerator(BaseGenerator):
    def generate(self, site, view):
        self.generate_article(site, view)
        self.generate_memo(site, view)

    def generate_article(self, site, view):
        tpl = os.path.join(site.theme, 'article_view.html')
        env = jinja2.Environment(
                loader = jinja2.FileSystemLoader(tpl),
                autoescape=True)
        with open(view.content['Path'], 'w') as f:
            f.write(tpl.render(site, view, doc))

    def generate_memo(self, site, view):
        tpl = os.path.join(site.theme, 'memo_view.html')
        env = jinja2.Environment(
                loader = jinja2.FileSystemLoader(tpl),
                autoescape=True)
        with open(view.content['Path'], 'w') as f:
            f.write(tpl.render(site, view, doc))

