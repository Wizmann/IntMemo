# coding=utf-8
from IntMemo.views import MemoView
from IntMemo.views import FlatView
from IntMemo.site  import Site

class MyMemoView(MemoView):
    path = 'content/memo'
    review_period = [1, 2, 4, 7, 15]

class AboutView(FlatView):
    path = 'content/about.md'

class MySite(Site):
    name = "IntMemo"
    template = 'default'



# update
# commit
# publish


