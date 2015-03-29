# coding=utf-8
import sys
import logging
from optparse import OptionParser

from View import MemoView
from View import FlatView
from View import memo_views

from Site  import Site
from TaskMgr import TaskMgr


formatter_str = "[%(asctime)s] %(levelname)s - [ %(filename)s : %(lineno)d ] : %(message)s"
logger = logging.getLogger()
s_handler = logging.StreamHandler()
s_formatter = logging.Formatter(formatter_str)
s_handler.setFormatter(s_formatter)
logger.addHandler(s_handler)
logger.setLevel(logging.NOTSET)

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
    parser.add_option('-m', dest='message')

    (options, args) = parser.parse_args()

    site = MySite()
    if options.gen:
        site.generate()
    elif options.add and options.view and options.message:
        for view in memo_views:
            if view.name == options.view.strip():
                task_mgr = TaskMgr(view, options.add)
                task_mgr.add_record(options.message)
                break
        else:
            logging.fatal("view name: %s not found" % options.view)


# update
# commit
# publish


