#coding=utf-8
import os
import logging
import json
import tempfile
import subprocess
import datetime
import jinja2

from Parser import parser

class TaskMgr(object):
    def __init__(self, view, taskid):
        self.view = view
        self.taskid = taskid

    def add_record(self, record):
        article = self.parse_article()
        self.do_add_record(article, record, self.view.review_period)
        self.dump_to_file(article)

    def do_add_record(self, article, record, review_period):
        process_section = {}
        for section in article:
            if section['section'] == '[Process]':
                process_section = section
            if section['section'] == '[Description]':
                desc = ''
                for item in section['content']:
                    if item.strip():
                        desc += item + '\n'
                    else:
                        desc += '\n'
                section['content'] = desc.strip()
        d = ''.join(process_section.get('content', '')).strip()
        if d:
            d = json.loads(''.join(d))
        else:
            d = {}
        idx = d.get('idx', 0)

        d['idx'] = idx + 1
        if d['idx'] >= len(review_period):
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

        if not process_section:
            process_section['section'] = '[Process]'
            article.append(process_section)
        process_section['content'] = json.dumps(d)
        print process_section

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
        path = os.path.join(self.view.path, self.taskid + '.md')
        with open(path) as article_file:
            article_str = article_file.read()
            article = parser.parse(article_str)
        return article

    def dump_to_file(self, article):
        path = os.path.join(self.view.path, self.taskid + '.md')
        r = self.dict_to_memo(article).encode('utf-8')
        with open(path, 'w') as article_file:
            article_file.write(r)

    def dict_to_memo(self, article):
        res = ''
        for section in article:
            res += section['section']
            res += '\n'
            if isinstance(section['content'], unicode) or \
                    isinstance(section['content'], str):
                res += section['content'].decode('utf-8')
            else:
                res += '\n'.join(
                    map(lambda x: x.decode('utf-8'), 
                        filter(lambda y: y, section['content']))).strip()
            res += '\n'
        return res

