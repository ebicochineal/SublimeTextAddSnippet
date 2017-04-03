#! /usr/bin/env python3

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
            s = self.view.substr(v[0])
            l = ''.join([x for x in s.lower() if 96 < ord(x) < 123])
            w = snippet % (s, s, l, scope)
            fpath = dir_scope + '/' + l + '.sublime-snippet'
            if not os.path.exists(dir) : os.mkdir(dir)
            if not os.path.exists(dir_scope) : os.mkdir(dir_scope)
            with open(fpath, 'w') as f : f.write(w)
            sublime.message_dialog(fpath + '\n' + w)
        except:
            pass