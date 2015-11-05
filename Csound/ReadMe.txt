v0.03 (Jan 07, 2013)
Takahiko Tsuchiya <ttsuchiya@berklee.edu>

This is a quick-made package for .csd in Sublime Text 2, with syntax highlighting, auto completion, opcode hint, and build system. It's only tested on Mac OSX. I'll prepare a public version on GitHub some time later, but feel free to modify these and repost.

To use, copy the folder /Csound into ST2's /Packages folder (on Mac, menu item Sublime Text 2 -> Preferences -> Browse Packages), and move the contents of another folder into /Packages/User folder.


// plugins
popup_hint.py: 
Shows the hint for the opcode at current cursor position in dialog window. Run it from context menu or set a shortcut key with "popup_hint" command.

statusbar_hint.py: 
Shows the hint in the status bar. Copy the .sublime-mousemap file to User folder, so the hint is shown automatically at mouse click.

search_in_manual.py:
Shows the opcode entry in online manual in browser. Open in brwoser is kind of buggy in ST2 in general.

open_in_csound_qt.py: 
Opens the current .csd file in CsoundQT (v0.7 Mac)


// build system (Mac)
Be careful not to run it twice. If the csd is set to run infinitely, it might not be able to stop.
