# Copyright 2010-2017 Luc Saffre
#
# License: BSD (see file COPYING for details)

"""
The :xfile:`models.py` file for this plugin.

"""

# This module is here e.g. for `lino.projects.docs` which installs the
# app but no BeIdCardHolder model.

from .choicelists import BeIdCardTypes, ResidenceTypes, CivilStates
from .mixins import BeIdCardHolder
