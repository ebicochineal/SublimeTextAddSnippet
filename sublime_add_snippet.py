#! /usr/bin/env python3

import os
import sublime
import sublime_plugin

dirname = 'MyAddedSnippet'
snippet = '<snippet>\n\t<description>%s</description>\n\t<content><![CDATA[%s]]></content>\n\t<tabTrigger>%s</tabTrigger>\n\t<scope>%s</scope>\n</snippet>'

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
            name = self.limitstr(self.toalpha(select_text), 12, False)
            trigger = self.limitstr(self.toalpha(select_text.split()[0]), 12, False)
            write_text = snippet % (description, select_text, trigger, scope)
            fpath = dir_scope + '/' + name + '.sublime-snippet'
            if not os.path.exists(dir) : os.mkdir(dir)
            if not os.path.exists(dir_scope) : os.mkdir(dir_scope)
            with open(fpath, 'w') as f : f.write(write_text)
            sublime.message_dialog(name + '\n\n' + fpath + '\n\n' + write_text)
        except:
            pass
    def limitstr(self, s, n, dot = True):
        if n <= 3 or dot == False:
            s = s[:n]
        elif len(s) > n:
            s = s[:n-3] + '...'
        return s
    def toalpha(self, s):
        return ''.join([(x if 96 < ord(x) < 123 else '') for x in s.lower()])
