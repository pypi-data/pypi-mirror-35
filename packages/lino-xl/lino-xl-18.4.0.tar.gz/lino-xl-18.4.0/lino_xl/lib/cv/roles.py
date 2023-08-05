# Copyright 2015 Luc Saffre
#
# License: BSD (see file COPYING for details)

from lino.api import _
from lino.core.roles import UserRole


class CareerUser(UserRole):
    text = _("CV user")


class CareerStaff(CareerUser):
    text = _("CV staff")


