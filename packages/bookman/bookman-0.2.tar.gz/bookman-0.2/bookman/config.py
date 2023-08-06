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

from enum import Enum
import sys
import os
import copy

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class FileMode(Enum):
    DEVELOPMENT = 1
    PRODUCTION_USER = 2
    PRODUCTION_LOCAL = 3
    PRODUCTION_SYSTEM = 4
    

class Config():
    CONFIG_BASENAME = 'config.yaml'
    
    PATH_TRIES = [ (os.environ["HOME"] + '/.bookman', FileMode.PRODUCTION_USER ),
                   ('.', FileMode.DEVELOPMENT),
                   ('/usr/local/share/bookman', FileMode.PRODUCTION_LOCAL),
                   ('/usr/share/bookman', FileMode.PRODUCTION_SYSTEM) ]
    

    def __init__(self):
        self.config = None
        self.full_config = None
        self.development_mode = False
        
        self.reload_config()
        
            
    def reload_config(self):
        """
        Reinitializes the object with a config file.
        
        Returns True if reloading was successful and False otherwise.
        """
        successful_reload = False
        
        self.development_mode = False

        path_tuple = self.try_paths(Config.CONFIG_BASENAME)
        if path_tuple != None:
            config_filename = path_tuple[0]
            
            if path_tuple[1] == FileMode.DEVELOPMENT:
                self.development_mode = True
            else:
                self.development_mode = False
    
            with open(config_filename, 'r') as file:
                self.full_config = load(file, Loader = Loader)
    
            if self.development_mode == False:
                self.set_config(copy.deepcopy(self.full_config["Environment"]["Production"]))
            else:
                self.set_config(copy.deepcopy(self.full_config["Environment"]["Development"]))
                
            successful_reload = True
            
        return successful_reload
            
        
    def try_paths(self, basename):
        """
        Returns a tuple with:
        1. The absolute filename for the basename
        2. The FileMode
        """
        ret_tuple = None
        
        for dirname in Config.PATH_TRIES:
            filename = dirname[0] + '/' + basename
            if os.path.isfile(filename):
                ret_tuple = (filename, dirname[1])
                break
            
        return ret_tuple
            
  
    def get_absolute_path(self, basename):
        return self.try_paths(basename)[0]
    
    
    def get_try_paths_dirname(self, file_mode : FileMode):
        for dirname in Config.PATH_TRIES:
            if dirname[1] == file_mode:
                return dirname[0]


    def get_config(self):
        return self.config
    
    
    def set_config(self, config):
        self.config = config
   
    
    def write_config_local(self):
        full_config = copy.deepcopy(self.full_config)
        full_config["Environment"]["Production"] = copy.deepcopy(self.get_config())
        
        config_dirname = self.get_try_paths_dirname(FileMode.PRODUCTION_USER)
        config_filename = config_dirname + '/' + Config.CONFIG_BASENAME
        
        if os.path.isdir(config_dirname) == False:
            os.mkdir(config_dirname)
        
        with open(config_filename, 'w') as file:
            dump(full_config, file) 


CONFIG_SINGLETON = Config()
