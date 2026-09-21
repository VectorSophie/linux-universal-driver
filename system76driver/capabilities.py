# system76-driver: Universal driver for System76 computers
# Copyright (C) 2005-2016 System76, Inc.
#
# This file is part of `system76-driver`.
#
# `system76-driver` is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# `system76-driver` is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with `system76-driver`; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""
Detect actual system capabilities instead of trusting a distro name.

`GrubAction` (see `actions.py`) already picks its backend by checking whether
`kernelstub` is present rather than by distro name; `has_command()` is that
same pattern, generalized so other actions can depend on it too.
"""

import shutil


def has_command(name):
    """Return True if `name` is an executable found on PATH."""
    return shutil.which(name) is not None
