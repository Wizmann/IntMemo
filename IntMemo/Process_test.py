#coding=utf-8
import unittest
import json

from Process import Processer

process1 = '{"nexttime": "2015-04-19", "records": [{"date": "2013-01-04", "comment": "the very first day"}, {"date": "2015-03-07", "comment": "the last day"}], "idx": 1}'


class TestProcess(unittest.TestCase):
    reivew_period = [0, 1, 2, 4, 7, 15]
    
    def test_add_record(self):
        article = {'Process': process1}
        p = Processer(article, self.reivew_period)
        text = p.add_record('the escapee will never stay')
        d = json.loads(article['Process'])
        self.assertEqual(d['idx'], 2)
        self.assertEqual(len(d['records']), 3)
        self.assertEqual(
                d['records'][2]['comment'],
                'the escapee will never stay')
        print d

if __name__ == '__main__':
    unittest.main()
