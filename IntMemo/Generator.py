#coding=utf-8
import sys
import os
import json
import jinja2
import time

import Filter

class Generator(object):
    def __new__(cls, name):
        if name == 'FlatView':
            return FlatViewGenerator()
        elif name == 'MemoView':
            return MemoViewGenerator()

class BaseGenerator(object):
    def generate(self, site, view):
        self.env = jinja2.Environment(
                loader=jinja2.FileSystemLoader(site.theme),
                autoescape=True)
        self.env.globals['nowts'] = \
                time.strftime(
                        '%Y-%m-%d %H:%M:%S %Z',
                        time.localtime(time.time()))
        json_handler = Filter.ArticleJsonHandler(site, view)
        self.env.filters['to_article_json'] = json_handler
        self.env.filters['join'] = Filter.join

class FlatViewGenerator(BaseGenerator):
    def generate(self, site, view):
        super(self.__class__, self).generate(site, view)
        path = os.path.join(site.output, view.output)
        tpl = self.env.get_template('flat_view.html')
        with open(path, 'w') as f:
            f.write(tpl.render(site=site, view=view).encode('utf-8'))

class MemoViewGenerator(BaseGenerator):
    def generate(self, site, view):
        super(self.__class__, self).generate(site, view)

        self.generate_article(site, view)
        self.generate_memo(site, view)

    def generate_article(self, site, view):
        tpl = self.env.get_template('article_view.html')
        output_path = os.path.join(site.output, view.name)
        if not os.path.exists(output_path):
            os.mkdir(output_path)

        for article in view.content:
            article_id = article['Metadata']['ID']
            path = os.path.join(output_path,
                    article_id + '.html')
            with open(path, 'w') as f:
                f.write(tpl.render(
                    site=site,
                    view=view,
                    article=article
                ).encode('utf-8'))

    def generate_memo(self, site, view):
        tpl = self.env.get_template('memo_view.html')
        path = os.path.join(site.output, view.output)
        tags = dict()
        for article in view.content:
            for (key, value) in article['Tags'].items():
                if key not in tags:
                    tags[key] = []
                tags[key] += value

        for (key, value) in tags.items():
            tags[key] = list(set(value))

        with open(path, 'w') as f:
            f.write(tpl.render(
                site=site,
                view=view,
                tags=tags,
            ).encode('utf-8'))

