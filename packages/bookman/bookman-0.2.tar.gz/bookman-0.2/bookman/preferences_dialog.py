# -*- coding: utf-8 -*-
################################################################################
# Copyright Richard Paul Bäck <richard.baeck@free-your-pc.com>, 2018
# This file is part of bookman.
#
# bookman is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# bookman is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with bookman.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import copy

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from . import CONFIG_SINGLETON

class PereferencesDialog:
    """
    Does not change the gloal config.
    """
    
    def __init__(self, app): 
        # Dialog
        self.dialog = None
       
        # Fields 
        self.doubleclick_execute_entry = None
        
        builder = Gtk.Builder()
        builder.set_translation_domain(app.appName)
        builder.add_from_file(CONFIG_SINGLETON.get_absolute_path(CONFIG_SINGLETON.get_config()["Builder"]["Files"]["PreferencesDialog"]))
        builder.connect_signals(self)
        
        self.init_dialog(builder)
        self.init_fields(builder)
        
    
    def init_dialog(self, builder : Gtk.Builder):
        self.dialog = builder.get_object('preferences_dialog')
        
        cancel_button = builder.get_object('cancel_button')
        cancel_button.connect("clicked", self.on_cancel_clicked)

        save_button = builder.get_object('save_button')
        save_button.connect("clicked", self.on_save_clicked)
        
        
    def init_fields(self, builder : Gtk.Builder):
        self.doubleclick_execute_entry = builder.get_object('doubleclick_execute_entry')
    
        
    def on_cancel_clicked(self, button : Gtk.Button):
        self.dialog.response(Gtk.ResponseType.CANCEL)
   
   
    def on_save_clicked(self, button : Gtk.Button):
        self.dialog.response(Gtk.ResponseType.OK)
        
        
    def config_to_gui(self, config, doubleclick_execute_entry : Gtk.Entry):
        doubleclick_execute_entry.set_text(config["Preferences"]["Doubleclick_Execute"])
        

    def gui_to_config(self, config, doubleclick_execute_entry : Gtk.Entry):
        config["Preferences"]["Doubleclick_Execute"] = doubleclick_execute_entry.get_text()

        
    def run(self):
        """
        If "Save" was clicked, then the changed copy of the global config is returned,
        otherwise None.
        """
        config = copy.deepcopy(CONFIG_SINGLETON.get_config())
       
        self.config_to_gui(config, self.doubleclick_execute_entry)
        
        response = self.dialog.run()
        
        if response != Gtk.ResponseType.OK:
            config = None
        else:
            self.gui_to_config(config, self.doubleclick_execute_entry)
            
        self.dialog.destroy()
   
        return config
    
