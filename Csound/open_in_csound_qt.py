import os
import sublime, sublime_plugin

class OpenInCsoundQtCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        view = sublime.Window.active_view(sublime.active_window())
        file = view.file_name()
        os.system("/Applications/CsoundQt-d-py-0.7.0.app/Contents/MacOS/CsoundQt-d-py " + file)

    def is_visible(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"

    def is_enabled(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"