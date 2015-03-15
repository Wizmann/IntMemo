# coding=utf-8
from View import MemoView
from View import FlatView
from Site  import Site

class MyMemoView(MemoView):
    path = 'content/memo'
    name = 'memo'
    title = 'Memo List'
    output = 'index.html'
    review_period = [1, 2, 4, 7, 15]

class AboutView(FlatView):
    path   = 'content/about.md'
    output = 'about.html'
    title   = 'About'

class MySite(Site):
    name     = "IntMemo"
    theme    = 'template/default'
    output   = 'publish'

if __name__ == '__main__':
    site = MySite()
    site.generate()


# update
# commit
# publish


