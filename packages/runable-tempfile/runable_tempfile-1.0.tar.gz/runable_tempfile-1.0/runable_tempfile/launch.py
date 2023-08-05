__author__ = 'unknown'
__url__ = 'https://pastebin.com/XVp46f7X'

import os
import subprocess
import sys


def launch(program):
    """launch(program)
     Run program or file as if it had been double-clicked in Finder, Explorer,
     Nautilus, etc. On OS X, the program should be a .app bundle, not a
     UNIX executable. When used with a URL, a non-executable file, etc.,
     the behavior is implementation-defined.

     Returns something false (0 or None) on success; returns something
     True (e.g., an error code from open or xdg-open) or throws on failure.
     However, note that in some cases the command may succeed without
     actually launching the targeted program.

     -------------------------------------------------------------------------
     Code downloaded from https://pastebin.com/XVp46f7X
     """
    if sys.platform == 'darwin':
        ret = subprocess.call(['open', program])
    elif sys.platform.startswith('win'):
        ret = os.startfile(os.path.normpath(program))
    else:
        ret = subprocess.call(['xdg-open', program])
    return ret
