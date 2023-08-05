# -*- coding: UTF-8 -*-
# Copyright 2015-2017 Luc Saffre
# This file is part of Lino Welfare.
#
# Lino Welfare is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Welfare is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Welfare.  If not, see
# <http://www.gnu.org/licenses/>.

"""
"""

from builtins import range
from lino.utils import Cycler
from lino.api import rt

from lino_xl.lib.clients.choicelists import ClientStates

def objects():

    Obstacle = rt.models.cv.Obstacle
    ObstacleType = rt.models.cv.ObstacleType
    Client = rt.models.pcsw.Client

    CLIENTS = Cycler(Client.objects.filter(
        client_state=ClientStates.coached)[10:15])

    TYPES = Cycler(ObstacleType.objects.all())

    for i in range(20):
        yield Obstacle(person=CLIENTS.pop(), type=TYPES.pop())
