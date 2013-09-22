import sublime, sublime_plugin
import os.path

class SwitchAspxCsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name, ext = os.path.splitext(self.view.file_name())
        win = self.view.window()
        if ext == ".aspx":
            win.open_file(name+".aspx.cs")
        elif ext == ".ascx":
            win.open_file(name+".ascx.cs")            
        elif ext == ".master":
            win.open_file(name+".master.cs")
        elif ext == ".cs":
            name2, ext2 = os.path.splitext(name)
            if ext2 == ".designer":
                win.open_file(name2)
            else: 
                win.open_file(name)

class SwitchAspxDesignerCsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name, ext = os.path.splitext(self.view.file_name())
        win = self.view.window()
        if ext == ".aspx":
            win.open_file(name+".aspx.designer.cs")
        elif ext == ".cs":
            name2, ext2 = os.path.splitext(name)
            if ext2 == ".designer":
                win.open_file(name2)
            else: 
                win.open_file(name)
