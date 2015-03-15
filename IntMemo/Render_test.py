#coding=utf-8
import unittest

from Render import Renderer

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

class TestRender(unittest.TestCase):
    def test_markdown_renderer(self):
        renderer = Renderer('Markdown')
        doc = '# Hello World'
        self.assertEqual(
                renderer.render(doc),
                '<h1>Hello World</h1>\n')
    
    def test_memo_renderer(self):
        renderer = Renderer('Memo')
        res = renderer.render(memo1, '/path/to/fake.md')
        self.assertEqual(res['Metadata']['ID'], 'fake')
        self.assertEqual(res['Metadata']['date'], '2015-03-07')
        self.assertEqual(res['Tags']['difficulty'], ['5'])

if __name__ == '__main__':
    unittest.main()
