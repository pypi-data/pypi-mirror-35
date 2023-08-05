# Copyright 2016 Alex Orange
# 
# This file is part of LDB Setuptools Coverage.
# 
# LDB Setuptools Coverage is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# LDB Setuptools Coverage is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with LDB Setuptools Coverage.  If not, see <http://www.gnu.org/licenses/>.

import unittest

import my_pkg.mod
import ns_pkg.pkg.mod

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3+4, my_pkg.mod.sum(3,4))

    def test2(self):
        self.assertEqual(3+4, ns_pkg.pkg.mod.sum(3,4))
