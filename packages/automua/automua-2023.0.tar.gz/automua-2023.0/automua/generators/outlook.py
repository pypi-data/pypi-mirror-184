"""
automua™ is a trademark of "Gaspard d'Hautefeuille" and may not be used 
by third parties without the prior written permission of the author.

Dev notes: we keep the SSL element as the Thunderbird autodiscovery process does not support yet the Encryption element
See: https://bugzilla.mozilla.org/show_bug.cgi?id=1799635

Copyright © 2022 Gaspard d'Hautefeuille: fix Autodiscover requests, replace SSL by TLS, consider Thunderbird bug
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
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

from automua import DomainNotFound
from automua import InvalidServerType
from automua.generators import ConfigGenerator
from automua.generators import xml_to_string
from automua.ldap import LookupResult
from automua.ldap import STATUS_SUCCESS
from automua.model import Davserver
from automua.model import Domain
from automua.model import Server
from automua.util import expand_placeholders
from automua.util import socket_type_needs_tls

NS_REQUEST = 'http://schemas.microsoft.com/exchange/autodiscover/outlook/requestschema/2006'
NS_RESPONSE_ROOT = 'http://schemas.microsoft.com/exchange/autodiscover/responseschema/2006'
NS_RESPONSE_PAYLOAD = 'http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a'

DAVSERVER_TYPE_MAP = {
    'caldav': 'CalDAV',
    'carddav': 'CardDAV'
}
SERVER_TYPE_MAP = {
    'imap': 'IMAP',
    'pop': 'POP3',
    'smtp': 'SMTP'
}


class OutlookGenerator(ConfigGenerator):
    """Configuration generator for Outlook et al.

    See https://support.microsoft.com/en-us/help/3211279/outlook-2016-implementation-of-autodiscover
    """

    @staticmethod
    def on_off(condition: bool) -> str:
        if condition:
            return 'on'
        return 'off'

    def davserver_element(self, parent: Element, server: Davserver, login_name: str) -> None:
        element = SubElement(parent, 'Protocol')
        SubElement(element, 'Type').text = DAVSERVER_TYPE_MAP[server.type]
        SubElement(element, 'Server').text = server.url
        if server.port > 0:
            SubElement(element, 'Port').text = str(server.port)
        if server.use_ssl:
            SubElement(element, 'SSL').text = 'on'       
            SubElement(element, 'Encryption').text = 'TLS'
        else:
            SubElement(element, 'SSL').text = 'off'       
            SubElement(element, 'Encryption').text = 'None'
        SubElement(element, 'DomainRequired').text = self.on_off(server.domain_required)
        if login_name:
            SubElement(element, 'LoginName').text = login_name

    def mailserver_element(self, parent: Element, server: Server, login_name: str) -> None:
        element = SubElement(parent, 'Protocol')
        SubElement(element, 'Type').text = SERVER_TYPE_MAP[server.type]
        SubElement(element, 'Server').text = server.name
        SubElement(element, 'Port').text = str(server.port)
        SubElement(element, 'LoginName').text = login_name
        SubElement(element, 'SSL').text = self.on_off(socket_type_needs_tls(server.socket_type))
        SubElement(element, 'Encryption').text = server.socket_type

    @staticmethod
    def user_element(parent: Element, display_name: str) -> None:
        element = SubElement(parent, 'User')
        SubElement(element, 'DisplayName').text = display_name

    def client_config(self, local_part, domain_part: str, display_name: str) -> str:
        domain: Domain = Domain.query.filter_by(name=domain_part).first()
        root_element = Element('Autodiscover', attrib={'xmlns': NS_RESPONSE_ROOT})
        response = SubElement(root_element, 'Response', attrib={'xmlns': NS_RESPONSE_PAYLOAD})
        if not domain:
            raise DomainNotFound(f'Domain "{domain_part}" not found')
        if domain.ldapserver:
            lookup_result: LookupResult = self.ldap_lookup(f'{local_part}@{domain_part}', domain.ldapserver)
        else:
            lookup_result = LookupResult(STATUS_SUCCESS, display_name, None)
        if lookup_result.cn:
            self.user_element(response, lookup_result.cn)
        account = SubElement(response, 'Account')
        # Mandatory mail servers
        SubElement(account, 'AccountType').text = 'email'
        SubElement(account, 'Action').text = 'settings'
        for server in self.servers_by_prio(domain.servers):
            if server.type not in SERVER_TYPE_MAP:
                raise InvalidServerType(f'Invalid server type "{server.type}"')
            name = expand_placeholders(self.pick_one(server.user_name, lookup_result.uid), local_part, domain_part)
            self.mailserver_element(account, server, name)
        # Optional DAV servers
        for server in domain.davservers:
            if server.type not in DAVSERVER_TYPE_MAP:  # pragma: no cover
                raise InvalidServerType(f'Invalid DAV server type "{server.type}"')
            name = expand_placeholders(self.pick_one(server.user_name, lookup_result.uid), local_part, domain_part)
            self.davserver_element(account, server, name)
        return xml_to_string(root_element)
