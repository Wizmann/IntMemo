#coding=utf-8
import os
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
                return '\n<pre><code>%s</code></pre>\n' \
                        % cgi.escape(text.strip())
            lexer = pygments.lexers.get_lexer_by_name(lang, stripall=True)
            formatter = pygments.formatters.HtmlFormatter()
            return pygments.highlight(text, lexer, formatter)

    def render(self, doc):
        renderer = self.BleepRenderer()
        misaka_md = misaka.Markdown(renderer,
            extensions=misaka.EXT_FENCED_CODE | misaka.EXT_NO_INTRA_EMPHASIS)
        return misaka_md.render(doc.strip().decode('utf-8'))

class MemoRenderer(BaseRenderer):
    MemoSections = [
            'Metadata',
            'Tags',
            'Description',
            'Process',
    ]
    def render(self, doc, path):
        res = {}
        d = dict(map(lambda x: (x['section'], x['content']), 
                parser.parse(doc.strip())))
        if '[Process]' not in d:
            d['[Process]'] = ''

        tags = set([])

        for section in self.MemoSections:
            s = '[' + section + ']'
            assert s in d, "Section(%s) not in doc(%s)" % (section, path)
            res[section] = d[s]

        res['Tags']        = self.render_tags(res['Tags'])
        res['Process']     = self.render_process(res['Process'])
        res['Description'] = self.render_desc(res['Description'])
        res['Metadata']    = self.render_meta(res['Metadata'])

        basename = os.path.basename(path)
        res['Metadata']['ID'] = basename[:basename.rfind('.')]

        return res

    def render_process(self, process):
        return (''.join(process)).strip()

    def render_desc(self, desc):
        renderer = Renderer('Markdown')
        return renderer.render(''.join(desc))

    def render_tags(self, tags):
        d = {}
        for line in tags:
            line = line.strip()
            if not line:
                continue
            (key, value) = map(lambda x: x.strip(),
                    line.split(':'))
            d[key] = map(lambda x: x.strip(), value.split(','))
        return d

    def render_meta(self, meta):
        d = {}
        for line in meta:
            line = line.strip()
            if not line:
                continue
            (key, value) = map(lambda x: x.strip(),
                    line.split(':'))
            d[key] = value
        return d

