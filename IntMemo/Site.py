#coding = utf-8
import Generator
import View

class Site(object):
    def generate(self):
        flat_gen = Generator(self, "FlatView")
        for view in View.flat_views:
            flat_gen.generate(view)

        memo_gen = Generator(self, "MemoView")
        for view in View.memo_views:
            memo_gen.generate(view)
