#coding=utf-8
import unittest

from Parser import parser
from Parser import lexer

memo1 = '''
[Metadata]
date: 2015-03-07
title: 你很重要，打比赛已经不行了。我得去造个轮子

[Tags]
categories: python, angularjs, love
difficulty: 5

[Description]
我觉得我已经没有什么潜力可挖了。突然感到有些腻烦。

对于我来说，并不可以谈生活。因为我见到过巫师的水晶球，我向里面看了一眼。

从此不能自拔。

[Process]
# DO NOT EDIT THE THINGS BELOW UNLESS YOU KNOW EXACTLY WHAT YOU ARE DOING
{"date": "2013-01-04", "comment": "Only work no play, make Jake a dull boy."}
'''

class TestParser(unittest.TestCase):
    def test_lexer(self):
        lexer.input("[maerlyn's]\n[rainbow]")
        self.assertEqual('SECTION', lexer.token().type)
        self.assertEqual('CR',      lexer.token().type)
        self.assertEqual('SECTION', lexer.token().type)

    def test_parser(self):
        result = parser.parse(memo1.strip())
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0]['section'], '[Metadata]')
        self.assertEqual(result[1]['section'], '[Tags]')
        self.assertEqual(result[2]['section'], '[Description]')
        self.assertEqual(result[3]['section'], '[Process]')

if __name__ == '__main__':
    unittest.main()
