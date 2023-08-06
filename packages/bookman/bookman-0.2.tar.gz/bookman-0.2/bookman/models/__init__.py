# -*- coding: utf-8 -*-
################################################################################
# Copyright Richard Paul Baeck <richard.baeck@free-your-pc.com>, 2018
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

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from .base import Base
from .tag import Tag
from .folder import Folder
from .bookmark import Bookmark
from .database_singleton import DATABASE_SINGLETON

__all__ = ( 'Base',
            'Bookmark', 'Tag', 'Folder',
            'DATABASE_SINGLETON')
