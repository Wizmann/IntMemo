# coding=utf-8
import sys
from optparse import OptionParser

from View import MemoView
from View import FlatView
from View import memo_views

from Site  import Site
from TaskMgr import TaskMgr

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
    parser = OptionParser()

    parser.add_option('-g', action='store_true', dest='gen')
    parser.add_option('-a', dest='add')
    parser.add_option('-v', dest='view')

    (options, args) = parser.parse_args()

    site = MySite()
    if options.gen:
        site.generate()
    elif options.add and options.view:
        for view in memo_views:
            if view.name == options.view:
                task_mgr = TaskMgr(view, options.add)
                task_mgr.add_record()
        else:
            logging.fatal("view name: %s not found" % options.view)


# update
# commit
# publish


