import webbrowser
import sublime, sublime_plugin

class SearchInManualCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        word = self.view.substr(self.view.word((self.view.sel()[0].b)))
        webbrowser.open_new_tab("http://www.csounds.com/manual/html/%s" % word)

    def is_visible(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"
        
    def is_enabled(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"
