# -*- coding: utf-8 -*-
################################################################################
# Copyright Richard Paul Bäck <richard.baeck@free-your-pc.com>, 2018
# This file is part of bookman.
#
# SambaConnector is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SambaConnector is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with bookman.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import os

import gettext
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio,Gtk

from .main_window import MainWindow

class BookmanApplication(Gtk.Application):
    appName = "bookman"
    window = None

    def __init__(self, args):
        gettext.bindtextdomain(self.appName)
        gettext.textdomain(self.appName)
        _ = gettext.gettext

        Gtk.Application.__init__(self, application_id="com.free-your-pc.bookman",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.window = MainWindow(self)

    def do_activate(self):
        self.window.show()
