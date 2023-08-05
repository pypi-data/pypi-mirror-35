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

"""Some test cases for :mod:`lino_welfare.modlib.debts`.

How to run only this test::

  $ go welfare
  $ cd lino_welfare/projects/std
  $ python manage.py test tests.test_households

"""

from __future__ import unicode_literals
from __future__ import print_function

import logging
logger = logging.getLogger(__name__)

import os
import json
from bs4 import BeautifulSoup

from lino.utils.djangotest import RemoteAuthTestCase
from lino.utils import AttrDict

from django.conf import settings
from lino.modlib.users.choicelists import UserTypes
from lino.api.shell import countries, pcsw, users


def readfile(name):
    fn = os.path.join(os.path.dirname(__file__), name)
    return open(fn).read()


class BeIdTests(RemoteAuthTestCase):
    maxDiff = None
    # override_djangosite_settings = dict(use_java=True)

    def test01(self):

        # is it the right settings module?
        self.assertEqual(os.environ['DJANGO_SETTINGS_MODULE'],
                         'lino_welfare.projects.std.settings.demo')

        self.assertEqual(settings.MIDDLEWARE_CLASSES, (
            'django.middleware.common.CommonMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'lino.core.auth.middleware.AuthenticationMiddleware',
            'lino.core.auth.middleware.WithUserMiddleware',
            'lino.core.auth.middleware.DeviceTypeMiddleware',
            'lino.core.auth.middleware.RemoteUserMiddleware',
            'lino.utils.ajax.AjaxExceptionResponse'))

        u = users.User(username='root',
                       user_type=UserTypes.admin,
                       language="en")
        u.save()
        self.client.force_login(u)
        be = countries.Country(name="Belgium", isocode="BE")
        be.save()
        kw = dict()
        # kw.update(card_number="123456789")
        # kw.update(national_id="680601 053-29")
        kw.update(id=116)
        kw.update(first_name="Jean")
        kw.update(middle_name="Jacques")
        kw.update(last_name="Jeffin")
        obj = pcsw.Client(**kw)
        obj.full_clean()
        obj.save()

        from lino_xl.lib.households.fixtures.std import objects
        for o in objects():
            o.save()

        # FIRST TEST : helped me to understand a problem on 20150130
        # ("Submitting an ActionFormPanel no longer forwards
        # `param_values`").  Since the problem was caused by
        # Javascript code in :xfile:`linoweb.js`, it cannot
        # actually reproduce the problem (that would
        # require a Javascript testing framework).

        # Reception --> Clients --> Detail on client 116

        url = "/api/reception/Clients/116?"
        # url += "pv=&pv=&pv=&pv=&pv=false&pv=&pv=&pv=&pv=&pv=&pv=10&pv=false"
        url += "&an=detail&rp=ext-comp-1359&fmt=json"

        response = self.client.get(url, REMOTE_USER='root')
        result = self.check_json_result(
            response, 'navinfo data disable_delete id title')

        fieldname = 'households_MembersByPerson'
        html = result['data'][fieldname]
        soup = BeautifulSoup(html, 'lxml')
    
        links = soup.find_all('a')
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0].string, 'Join an existing household')
        self.assertEqual(links[1].get_text(), 'create a new one')
        js = links[0]['href']
        start = "javascript:Lino.households.MembersByPerson.insert.run"
        self.assertEqual(js.startswith(start), True)
        
        js = links[1]['href']
        start = ('javascript:Lino.contacts.Persons.create_household.'
                 'run("ext-comp-1359",')
        self.assertEqual(js.startswith(start), True)
        js = js[len(start):-1]
        d = AttrDict(json.loads(js))

        self.assertEqual(
            ' '.join(sorted(d.keys())),
            'base_params field_values param_values record_id')
        self.assertEqual(len(d.field_values), 6)
        self.assertEqual(
            list(sorted(d.field_values.keys())), 
            ['head', 'headHidden',
             'partner', 'partnerHidden',
             'type', 'typeHidden'])
        self.assertEqual(len(d.param_values), 18)
        self.assertEqual(len(d.base_params), 0)

        fv = AttrDict(d.field_values)
        self.assertEqual(fv.head, 'JEFFIN Jean (116)')

        pv = AttrDict(d.param_values)
        self.assertEqual(pv.also_obsolete, False)
        self.assertEqual(pv.gender, None)
        self.assertEqual(pv.genderHidden, None)

        # When user klicks OK:
        url = "/api/contacts/Persons/116"
        url += "?fv=116&fv=&fv=1&an=create_household"

        # The 20150130 problem was because the ActionFormPanel added
        # param_values. When klicking OK, it sometimes added the
        # following:
        if False:  # before 20150130
            url += "&pv=&pv=&pv=&pv=&pv=false&pv=&pv=&pv=&pv=&pv=&pv=10&pv=false"
        url += "&sr=116"
        response = self.client.get(url, REMOTE_USER='root')
        result = self.check_json_result(
            response, 'message success refresh_all close_window')


