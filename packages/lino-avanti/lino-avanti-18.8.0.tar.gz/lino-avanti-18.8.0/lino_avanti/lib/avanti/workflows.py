# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
#
# License: BSD (see file COPYING for details)

"""Default workflows for Lino Avanti.

This can be used as :attr:`workflows_module
<lino.core.site.Site.workflows_module>`

"""

# calendar events and presences:
from lino_xl.lib.cal.workflows.voga import *
# from lino_xl.lib.cal.workflows import feedback

from lino_avanti.lib.courses.workflows import *

from lino.api import _

from lino_xl.lib.clients.choicelists import KnownContactTypes
KnownContactTypes.clear()
add = KnownContactTypes.add_item

add('10', _("Health insurance"), 'health_insurance')
add('20', _("School"), 'school')
add('30', _("Pharmacy"), 'pharmacy')
add('40', _("General social assistant"), 'general_assistant')
add('50', _("Integration assistant"), 'integ_assistant')
add('60', _("Work consultant"), 'work_consultant')
