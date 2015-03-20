#coding=utf-8
import os
import json
import tempfile
import subprocess
import datetime
import jinja2

from Parser import parser

class TaskMgr(object):
    def __init__(self, site, taskid):
        self.site = site
        self.taskid = taskid

    def add_record(self):
        record = self.get_record()
        article = self.parse_article(self.site, self.taskid)

        self.do_add_record(article, record)
        self.dump_to_file(article)

    def do_add_record(self, article, record, review_period):
        if 'Process' in article:
            d = json.loads(article['Process'])
        else:
            d = {}
        
        idx = d.get('idx', 0)

        d['idx'] = idx + 1
        if d['idx'] == len(review_period):
            d['nexttime'] = ''
        else:
            delta = review_period[idx + 1] - \
                    review_period[idx]
            d['nexttime'] = (
                    datetime.date.today()
                    + datetime.timedelta(delta)
            ).strftime('%Y-%m-%d')
        records = d.get('records', [])
        records.append({
                'date': datetime.date.today().strftime('%Y-%m-%d'),
                'comment': record,
        })
        d['records'] = records

        article['Process'] = d

    def get_record(self):
        EDITOR = os.environ.get('EDITOR','vim') 

        initial_msg = ''
        with tempfile.NamedTemporaryFile(suffix=".tmp") as tmpfile:
            tmpfile.write(initial_msg)
            tmpfile.flush()
            subprocess.call([EDITOR, tmpfile.name])
            tmpfile.seek(0)
            record = tmpfile.read()
        return record

    def parse_article(self):
        path = os.path.join(self.site.path, self.taskid + '.md')
        with open(path) as article_file:
            article = parser.parse(article_file.read().strip())
        return article

    def dump_to_file(self, article):
        path = os.path.join(self.site.path, self.taskid + '.md')
        with open(path, 'w') as article_file:
            article_file.write(dict_to_memo(article))

    def dict_to_memo(self, article):
        env = jinja2.Environment(
                os.path.dirname(os.path.abspath(__file__)))
        env.filter['to_json'] = lambda x: json.dumps(x)
        tpl = env.get_template('memo.tpl')
        return tpl.render(article)

