#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 The MUSSLES developers
#
# This file is part of MUSSLES.
#
# MUSSLES is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MUSSLES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MUSSLES.  If not, see <http://www.gnu.org/licenses/>.

# ===============================================================================
#         Command Line
# ===============================================================================
from .cli import cli_main

# ===============================================================================
#         Distributions
# ===============================================================================
from .distributions import normal_logpost
from .distributions import gev_logpost

# ===============================================================================
#         Gelman & Rubin
# ===============================================================================
from .gelman_rubin import GR_result
