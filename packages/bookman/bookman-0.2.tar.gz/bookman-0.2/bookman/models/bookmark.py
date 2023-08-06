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

import copy
import re

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref

from . import Base
from . import Folder
from . import Tag

BOOKMARK_TAG_LINK_TABLE = Table('bookmark_tag_link', Base.metadata,
    Column('bookmark_id', Integer, ForeignKey('bookmark.id')),
    Column('tag_id', Integer, ForeignKey('tag.id'))
)

class Bookmark(Base):
    __tablename__ = 'bookmark'
    
    id = Column(Integer, primary_key = True)
    
    name = Column(String(250), nullable = False)
    
    url = Column(String(250), nullable = False)
    
    description = Column(String(99999), nullable = False)

    folder_id = Column(Integer, ForeignKey('folder.id'))
    # folder = relationship(
    #     Folder,
    #    backref = backref('folders',
    #                      uselist=True,
    #                      cascade='delete,all')) 
    
    tags = relationship("Tag", secondary = BOOKMARK_TAG_LINK_TABLE,
                        lazy = 'joined')
    
 
    def copy(self, other):
        self.id = other.id
        self.name = other.name
        self.url = other.url
        self.description = other.description
       
        self.tags = [ ] 
        for other_tag in other.tags:
            tag = Tag(name = '')
            tag.copy(other_tag)
            self.tags.append(tag)
        
        
    def fuzzy_search(self, keyword : str):
        """
        Returns True if keyword is in any value of this Bookmark. Returns False otherwise.
        """
        matches = False
       
        if keyword is None or len(keyword) == 0:
            matches = True
        elif keyword[0] == '#':
            search_for_tag = keyword[1 : ]
            for tag in self.tags:
                if tag.name == search_for_tag:
                    matches = True
                    break
        else:
            regex = re.compile(keyword) 
            if regex.search(self.name) or regex.search(self.url) or regex.search(self.description):
                matches = True
                
        return matches
        