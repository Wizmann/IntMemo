#coding=utf-8
import unittest

import View

class FlatViewDemo(View.FlatView):
    path = 'path/to/demo.md'

class MemoViewDemo(View.MemoView):
    path = 'path/to/memo'

class TestView(unittest.TestCase):
    def test_flat_view(self):
        self.assertEqual(len(View.flat_views), 1)

        view = View.flat_views[0]
        self.assertEqual(view.path, 'path/to/demo.md')

    def test_memo_view(self):
        self.assertEqual(len(View.memo_views), 1)

        view = View.memo_views[0]
        self.assertEqual(view.path, 'path/to/memo')

if __name__ == '__main__':
    unittest.main()
