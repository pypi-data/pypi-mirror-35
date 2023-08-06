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

from distutils.core import setup

setup(
    name = "bookman",
    version = "0.2",
    author = "Richard Paul Baeck",
    author_email = "richard.baeck@free-your-pc.com",
    license = "GPLv2",
    description = ("A tool to manage your bookmarks."),
    long_description = open("README.md").read(),
    packages = [ "bookman",
                 "bookman.models"],
    scripts = [ "bookman-gui" ],
    data_files = [ ( "share/bookman",
                    [ "config.yaml" ] ),
                   ( "share/bookman/ui",
                    [ "ui/main_window.glade",
                      "ui/preferences_dialog.glade" ] ),
                   ( "share/locale/de/LC_MESSAGES",
                    [ "locale/de/LC_MESSAGES/bookman.mo" ] ),
                   ("share/locale/en/LC_MESSAGES",
                    ["locale/en/LC_MESSAGES/bookman.mo"] ) 
                 ],
    install_requires=[ "SQLAlchemy", "PyYAML" ]
)
