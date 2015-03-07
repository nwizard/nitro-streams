# -*- coding: latin-1 -*-

import xbmcgui

class DialogInfo:

    def __init__(self):
        self.dlg = xbmcgui.Dialog()
        self.head = '[COLOR=FF00FF00]Nitro Streams Info[/COLOR]'

    def show(self, message):
        self.dlg.ok(self.head, message)