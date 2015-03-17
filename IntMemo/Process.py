#coding=utf-8
import datetime
import json

class Processer(object):
    def __init__(self, article, review_period):
        self.article = article
        self.review_period = review_period

    def add_record(self, comment):
        d = {}
        if 'Process' in self.article:
            d = json.loads(self.article['Process'])
        
        idx = d.get('idx', 0)

        d['idx'] = idx + 1
        if d['idx'] == len(self.review_period):
            d['nexttime'] = ''
        else:
            delta = self.review_period[idx + 1] - \
                    self.review_period[idx]
            d['nexttime'] = (
                    datetime.date.today()
                    + datetime.timedelta(delta)
            ).strftime('%Y-%m-%d')
        records = d.get('records', [])
        records.append({
                'date': datetime.date.today().strftime('%Y-%m-%d'),
                'comment': comment,
        })
        d['records'] = records
        self.article['Process'] = json.dumps(d)



