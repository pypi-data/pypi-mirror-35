import os
import re

# 3rd party
from slugify import slugify
import pygments
from pygments import highlight
from pygments.lexers.c_cpp import CppLexer
from pygments.lexers import guess_lexer_for_filename
import itertools
from collections import OrderedDict
from fs.osfs import OSFS

from .html import HtmlFormatter, get_style
from .templates import *
from .filetree import make_file_tree, SourceFile

class CodeReport:
    def __init__(self, items, encoding="utf-8", 
                 title="Code Report", srcfs=OSFS('/'), destfs = OSFS('/'),
                 rootdir="/"):
        self._items = items
        self._title = title
        self._encoding = encoding
        self._srcfs = srcfs
        self._destfs = destfs
        self._rootdir = rootdir

        self._srcfiles = []

    def render(self, destdir):
        kf = lambda i: os.path.normpath(i.path)
        for file, items in itertools.groupby(sorted(self._items, key=kf), kf):
            items = list(items)
            def normpath(s):
                out = s
                if s.startswith(self._rootdir):
                    out = s[len(self._rootdir):]
                return os.path.normpath(out)
            srcfile = SourceFile(items[0].path, normpath=normpath)
            srcfile.add_items(items)
            self._srcfiles.append(srcfile)

        self._filetree = make_file_tree(self._srcfiles)

        self._destfs.makedir(destdir, recreate=True)

        for sf in self._srcfiles:
            with self._destfs.open(os.path.join(destdir, sf.report_file_name), "w+") as f:
                f.write(self._render_code_file(sf))

        with self._destfs.open(os.path.join(destdir, "index.html"), "w+") as f:
            f.write(self._render_index())
        
        with self._destfs.open(os.path.join(destdir, "index_summary.html"), "w+") as f:
            f.write(self._render_summary(self._items, standalone=True))

    def _render_code_file(self, srcfile):
        with self._srcfs.open(srcfile.raw_path, "r") as fh:
            raw_content = fh.read()

        try:
            lexer = guess_lexer_for_filename(srcfile.path, raw_content)
        except pygments.util.ClassNotFound:
            if srcfile.path.endswith(".ipp"):
                lexer = CppLexer()

        def get_comment(lineno):
            items = filter(lambda i: i.line == lineno, srcfile.items)
            return "\n\n".join(map(str, items))
            # msgs = self._get_comment(f, lineno, self)
            # if msgs is not None:
                # self._file_item_counts[f] += len(msgs)
                # return "\n".join(msgs)
            # return None

        code = highlight(raw_content, lexer, HtmlFormatter(get_comment))


        return file_tpl.render(srcfile=srcfile,
                               code=code,
                               summary=self._render_summary(srcfile.items),
                               title=self._title)


    def _render_index(self):
        return index_tpl.render(nodelist=[self._filetree],
                                summary=self._render_summary(self._items),
                                title=self._title)

    def _render_summary(self, items, standalone=False):
        kf = lambda i: i.code
        by_code = {}
        for item in items:
            if not item.code in by_code:
                by_code[item.code] = []
            by_code[item.code].append(item)

        by_code = OrderedDict(reversed(sorted(by_code.items(), key=lambda i: len(i[1]))))

        files = set([i.path for i in items])

        return summary_tpl.render(by_code=by_code,
                                  standalone=standalone,
                                  single_file=len(files) > 1)


