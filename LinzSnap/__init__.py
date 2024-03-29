#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       __init__.py
#
#       Copyright 2009 Chris Crook (ccrook@linz.govt.nz)
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from .Plugin import Plugin

def name():
    return Plugin.LongName

def description():
    return Plugin.Description

def version():
    return Plugin.Version

def qgisMinimumVersion():
    return Plugin.QgisMinimumVersion

def icon():
    return "./SnapLoader.png"

def authorName():
    return Plugin.Author

def classFactory(iface):
    return Plugin(iface)


