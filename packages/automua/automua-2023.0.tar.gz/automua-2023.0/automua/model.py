"""
automua™ is a trademark of "Gaspard d'Hautefeuille" and may not be used 
by third parties without the prior written permission of the author.

Copyright © 2022 Gaspard d'Hautefeuille: set default socket_type to TLS, replace legacy backref by back_populates
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

from flask_sqlalchemy import SQLAlchemy

from automua import PLACEHOLDER_ADDRESS

db = SQLAlchemy()

davserver_domain_map = db.Table(
    'davserver_domain',
    db.Column('davserver_id', db.Integer, db.ForeignKey('davserver.id'), primary_key=True),
    db.Column('domain_id', db.Integer, db.ForeignKey('domain.id'), primary_key=True)
)
server_domain_map = db.Table(
    'server_domain',
    db.Column('server_id', db.Integer, db.ForeignKey('server.id'), primary_key=True),
    db.Column('domain_id', db.Integer, db.ForeignKey('domain.id'), primary_key=True)
)


class Provider(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    short_name = db.Column(db.String(32), nullable=False)
    domains = db.relationship('Domain', lazy='select', back_populates='provider')

    def __repr__(self) -> str:
        return f'<Provider id={self.id} name={self.short_name}>'


class Server(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    prio = db.Column(db.Integer, nullable=False, server_default='10')
    name = db.Column(db.String(128), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(32), nullable=False)
    socket_type = db.Column(db.String(32), nullable=False, default='TLS')
    user_name = db.Column(db.String(64), nullable=False, default=PLACEHOLDER_ADDRESS)
    authentication = db.Column(db.String(32), nullable=False, default='plain')
    domains = db.relationship('Domain', secondary=server_domain_map, lazy='subquery', back_populates='servers')

    def __repr__(self) -> str:
        return f'<Server id={self.id} prio={self.prio} type={self.type} name={self.name}>'


class Davserver(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128), nullable=False)
    port = db.Column(db.Integer, nullable=False, default=0)
    type = db.Column(db.String(32), nullable=False)
    use_ssl = db.Column(db.Boolean, nullable=False)
    domain_required = db.Column(db.Boolean, nullable=False)
    user_name = db.Column(db.String(64), nullable=True)
    domains = db.relationship('Domain', secondary=davserver_domain_map, lazy='subquery', back_populates='davservers')

    def __repr__(self) -> str:
        return f'<Davserver id={self.id} type={self.type} url={self.url}>'


class Ldapserver(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    use_ssl = db.Column(db.Boolean, nullable=False)
    search_base = db.Column(db.String(128), nullable=False)
    search_filter = db.Column(db.String(128), nullable=False)
    attr_uid = db.Column(db.String(32), nullable=False)
    attr_cn = db.Column(db.String(32), nullable=True)
    bind_password = db.Column(db.String(128), nullable=True)
    bind_user = db.Column(db.String(128), nullable=True)
    domains = db.relationship('Domain', lazy='select', back_populates='ldapserver')

    def __repr__(self) -> str:
        return f'<Ldapserver id={self.id} name={self.name}>'


class Domain(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('provider.id'), nullable=False)
    ldapserver_id = db.Column(db.Integer, db.ForeignKey('ldapserver.id'), nullable=True)
    provider = db.relationship('Provider', lazy='joined', back_populates='domains')
    servers = db.relationship('Server', secondary=server_domain_map, lazy='select', back_populates='domains')
    davservers = db.relationship('Davserver', secondary=davserver_domain_map, lazy='select', back_populates='domains')
    ldapserver = db.relationship('Ldapserver', lazy='joined', back_populates='domains')



    def __repr__(self) -> str:
        return f'<Domain id={self.id} name={self.name}>'
