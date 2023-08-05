"""
automua™ is a trademark of "Gaspard d'Hautefeuille" and may not be used 
by third parties without the prior written permission of the author.

Copyright © 2019-2022 Ralph Seichter

This file is part of automua.

automua is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

automua is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with automua. If not, see <https://www.gnu.org/licenses/>.
"""
import unittest

from automua import LdapLookupError
from automua import LdapNoMatch
from automua.generators.apple import AppleGenerator
from automua.generators.mozilla import MozillaGenerator
from automua.generators.outlook import OutlookGenerator
from automua.database import LDAP_BIND_PASSWORD
from automua.database import LDAP_BIND_USER
from automua.database import LDAP_HOSTNAME
from automua.database import LDAP_PORT
from automua.database import LDAP_SEARCH_BASE
from automua.ldap import LdapAccess
from automua.ldap import LookupResult
from automua.ldap import STATUS_ERROR
from automua.ldap import STATUS_NO_MATCH
from automua.ldap import STATUS_SUCCESS
from automua.model import Ldapserver
from automua.util import unique
from tests.base import RUN_LDAP_TESTS
from tests.base import TestCase
from automua.server import create_app

app = create_app()

@unittest.skipUnless(RUN_LDAP_TESTS, 'Skipping LDAP tests')
class LdapTests(TestCase):
    """Tests for LDAP access methods."""
    EXISTS_LOCAL = 'a'
    EXISTS_DOMAIN = 'example.com'
    EXISTS_EMAIL = f'{EXISTS_LOCAL}@{EXISTS_DOMAIN}'
    EXISTS_CN = 'John Doe'
    EXISTS_UID = 'jd'
    UNIQUE = unique()
    ATTRIBUTES = {'attributes': {'x': [UNIQUE]}}

    @staticmethod
    def search_filter(email_address):
        return f'(mail={email_address})'

    def setUp(self) -> None:
        super().setUp()
        self.ldap = LdapAccess(hostname=LDAP_HOSTNAME, user=LDAP_BIND_USER, password=LDAP_BIND_PASSWORD, use_ssl=True)

    def test_attribute_exists(self):
        self.assertEqual(self.UNIQUE, self.ldap.get_attribute(self.ATTRIBUTES, 'x'))

    def test_attribute_missing(self):
        self.assertIsNone(self.ldap.get_attribute(self.ATTRIBUTES, 'y'))

    @unittest.skip  # Avoid triggering fail2ban
    def test_bind_failed(self):
        self.ldap = LdapAccess(hostname=LDAP_HOSTNAME, user=LDAP_BIND_USER, password=self.UNIQUE)
        x: LookupResult = self.ldap.lookup(LDAP_SEARCH_BASE, self.search_filter(self.EXISTS_EMAIL))
        self.assertEqual(STATUS_ERROR, x.status)

    def test_does_not_exist(self):
        x: LookupResult = self.ldap.lookup(LDAP_SEARCH_BASE, self.search_filter(self.UNIQUE))
        self.assertEqual(STATUS_NO_MATCH, x.status)

    def test_exists(self):
        x: LookupResult = self.ldap.lookup(LDAP_SEARCH_BASE, self.search_filter(self.EXISTS_EMAIL), attr_cn='cn')
        self.assertEqual(STATUS_SUCCESS, x.status)
        self.assertEqual(self.EXISTS_CN, x.cn)
        self.assertEqual(self.EXISTS_UID, x.uid)

    def test_apple_generator_ldap(self):
        with app.app_context():
            gen = AppleGenerator()
            gen.client_config(self.EXISTS_LOCAL, self.EXISTS_DOMAIN, '')

    def test_outlook_generator_ldap(self):
        with app.app_context():
            gen = OutlookGenerator()
            gen.client_config(self.EXISTS_LOCAL, self.EXISTS_DOMAIN, '')

    def test_mozilla_generator_ldap_exists(self):
        with app.app_context():
            server = Ldapserver.query.filter_by(id=LDAP_PORT).one()
            gen = MozillaGenerator()
            x = gen.ldap_lookup(self.EXISTS_EMAIL, server)
            self.assertEqual(STATUS_SUCCESS, x.status)

    def test_mozilla_generator_ldap_no_match(self):
        with app.app_context():
            server = Ldapserver.query.filter_by(id=LDAP_PORT).one()
            gen = MozillaGenerator()
            with self.assertRaises(LdapNoMatch):
                gen.ldap_lookup(self.UNIQUE, server)

    def test_mozilla_generator_ldap_missing_server(self):
        with self.assertRaises(LdapLookupError):
            gen = MozillaGenerator()
            gen.ldap_lookup(self.UNIQUE, None)


if __name__ == '__main__':
    unittest.main()
