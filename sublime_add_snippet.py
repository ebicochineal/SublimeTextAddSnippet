#! /usr/bin/env python3

import os
import sublime
import sublime_plugin

dirname = 'MyAddedSnippet'
snippet = '<snippet>\n\t<description>%s</description>\n\t<content><![CDATA[%s]]></content>\n\t<tabTrigger>%s</tabTrigger>\n\t<scope>%s</scope>\n</snippet>'

class addsnippetCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        v = self.view.sel()
        if v[0].empty():
            pass
        else:
            try:
                scope = self.view.scope_name(v[0].begin()).split()[0]
                dir = sublime.packages_path().replace('\\', '/') + '/' + dirname
                if not os.path.exists(dir) : os.mkdir(dir)
                s = self.view.substr(v[0])
                l = ''.join([x for x in s.lower() if 96 < ord(x) < 123])
                dir += '/' + scope.split('.')[1]
                fpath = dir + '/' + l + '.sublime-snippet'
                w = snippet % (s, s, l, scope)
                if not os.path.exists(dir) : os.mkdir(dir)
                with open(fpath, 'w') as f : f.write(w)
                sublime.message_dialog(fpath + '\n' + w)
            except:
                pass
