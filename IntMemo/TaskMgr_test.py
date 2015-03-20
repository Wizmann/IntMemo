#coding=utf-8
import unittest
import json

from TaskMgr import TaskMgr

process1 = '{"nexttime": "2015-04-19", "records": [{"date": "2013-01-04", "comment": "the very first day"}, {"date": "2015-03-07", "comment": "the last day"}], "idx": 1}'

class TestTaskMgr(unittest.TestCase):
    review_period = [0, 1, 2, 4, 7, 15]
    
    def test_do_add_record(self):
        article = {'Process': process1}
        p = TaskMgr(article, 'foo')
        p.do_add_record(article, 
                'the escapee will never stay',
                self.review_period)
        self.assertEqual(article['Process']['idx'], 2)
        self.assertEqual(len(article['Process']['records']), 3)
        self.assertEqual(
                article['Process']['records'][2]['comment'],
                'the escapee will never stay')

if __name__ == '__main__':
    unittest.main()
