#! /usr/bin/env python3

import os
import sublime
import sublime_plugin

dirname = 'MyAddedSnippet'
snippet = '<snippet>\n\t<description><![CDATA[%s]]></description>\n\t<content><![CDATA[%s]]></content>\n\t<tabTrigger>%s</tabTrigger>\n\t<scope>%s</scope>\n</snippet>'

class addsnippetCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view.sel()
        if v[0].empty() : return
        try:
            dir = sublime.packages_path().replace('\\', '/') + '/' + dirname
            scope = self.view.scope_name(v[0].begin()).split()[0]
            dir_scope = dir + '/' + scope.split('.')[1]
            select_text = self.view.substr(v[0])
            description = self.limitstr(select_text, 18)
            write_text = snippet % (description, select_text, self.totrigger(select_text), scope)
            fpath = dir_scope + '/' + self.toname(select_text) + '.sublime-snippet'
            if not os.path.exists(dir) : os.mkdir(dir)
            if not os.path.exists(dir_scope) : os.mkdir(dir_scope)
            with open(fpath, 'w') as f : f.write(write_text)
            sublime.message_dialog(self.toname(select_text) + '\n\n' + fpath + '\n\n' + write_text)
        except:
            pass
    def limitstr(self, s, n, dot = True):
        if n <= 3 or dot == False:
            s = s[:n]
        elif len(s) > n:
            s = s[:n-3] + '...'
        return s
    def toname(self, s):
        return self.limitstr(''.join([(x if 96 < ord(x) < 123 else '_') for x in s.lower()]), 12, False)
    def totrigger(self, s):
        r = ''
        for i in s.lower():
            if not 96 < ord(i) < 123 : break
            r += i
        return self.limitstr(r, 12, False)
