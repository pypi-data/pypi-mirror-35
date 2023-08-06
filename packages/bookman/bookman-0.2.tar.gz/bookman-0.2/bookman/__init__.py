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
# along with SambaConnector.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

from .config import CONFIG_SINGLETON
from .application import BookmanApplication

__all__ = ( 'BookmanApplication',
            'CONFIG_SINGLETON' )
