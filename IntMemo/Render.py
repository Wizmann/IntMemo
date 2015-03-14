#coding=utf-8
import cgi
import misaka
import pygments.lexers
import pygments.formatters

from Parser import parser

class Renderer(object):
    def __new__(cls, name):
        if name == 'Markdown':
            return MarkdownRenderer()
        elif name == 'Memo':
            return MemoRenderer()

class BaseRenderer(object):
    def renderer(self):
        raise NotImplementedError

class MarkdownRenderer(BaseRenderer):
    class BleepRenderer(misaka.HtmlRenderer, misaka.SmartyPants):
        def block_code(self, text, lang):
            if not lang:
                return '\n<pre><code>%s</code></pre>\n' 
                        % cgi.escape(text.strip())
            lexer = pygments.lexers.get_lexer_by_name(lang, stripall=True)
            formatter = pygments.formatters.HtmlFormatter()
            return pygments.highlight(text, lexer, formatter)

    def render(self, doc):
        renderer = BleepRenderer()
        misaka_md = misaka.Markdown(renderer,
            extensions=misaka.EXT_FENCED_CODE | misaka.EXT_NO_INTRA_EMPHASIS)
        return misaka_md.render(doc.strip())

class MemoRenderer(BaseRenderer):
    MemoSections = [
            'Metadata',
            'Description',
            'Process'
    ]
    def render(self, doc, path):
        d = parser.parse(doc)
        if 'Process' not in d:
            d['Process'] = ''
        for section in self.MemoSections
            s = '[' + section + ']'
            assert s in d, "Section(%s) not in doc(%s)" % (section, path)
            res[section] = d[s]
        sub_renderer = Renderer('Markdown')
        res['Description'] = sub_renderer.render(res['Description'])
        
        basename = os.path.basename(path)
        res['id'] = basename[:basename.rfind('.')]
        return res

