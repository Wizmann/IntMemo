#coding = utf-8
import View

from Generator import Generator

class Site(object):
    flat_views = View.flat_views
    memo_views = View.memo_views
    def generate(self):
        flat_gen = Generator("FlatView")
        for view in View.flat_views:
            view.process()
            flat_gen.generate(self, view)

        memo_gen = Generator("MemoView")
        for view in View.memo_views:
            view.process()
            memo_gen.generate(self, view)
