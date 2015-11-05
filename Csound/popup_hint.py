import sublime, sublime_plugin
import xml.etree.ElementTree as et

tree = et.parse('opcodes.xml')
root = tree.getroot()

def search(term):
    for catIndx, catEt in enumerate(root):
        for opcIndx, opcEt in enumerate(root[catIndx]):
            if len(opcEt) > 1:
                if opcEt[1][0].text == term:
                    return catIndx, opcIndx

def showHint(cat, opc):
    front = root[cat][opc][1].text
    if front == None:
        front = ""
    opcode = root[cat][opc][1][0].text
    tail = root[cat][opc][1][0].tail
    if tail == None:
        tail = ""
    desc = root[cat][opc][0].text
    opcodeName = "{0:^50}".format(opcode)
    return "%s\n\n%s<%s>%s\n\n%s" % (opcodeName, front, opcode, tail, desc)

class PopupHintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        word = self.view.substr(self.view.word((self.view.sel()[0].b)))
        cat = search(word)[0]
        opc = search(word)[1]
        sublime.message_dialog(showHint(cat, opc))

    def is_visible(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"
        
    def is_enabled(self):
        return self.view.file_name() and self.view.file_name()[-4:] == ".csd"
