#coding=utf-8
import json

class ArticleJsonHandler(object):
    def __init__(self, site, view):
        self.site = site
        self.view = view

    def __call__(self, article):
        tags = ['Metadata', 'Tags', 'Process']
        d = {}
        for tag in tags:
            if isinstance(article[tag], dict):
                for (key, value) in article[tag].items():
                    d[key.lower()] = value
            else:
                d[tag.lower()] = article[tag]
        d['process'] = '%d%%' % (
                100 * d['idx'] / len(self.view.review_period))
        d['url'] = '/'.join([
            self.view.name,
            d['id'] + '.html'
        ])
        return json.dumps(d)

def join(valuelist):
    return ' / '.join(map(str, valuelist))
