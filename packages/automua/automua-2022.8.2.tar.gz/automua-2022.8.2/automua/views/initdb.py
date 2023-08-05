"""
automua™ is a trademark of "Gaspard d'Hautefeuille" and may not be used 
by third parties without the prior written permission of the author.

Copyright © 2022 Gaspard d'Hautefeuille: gradual migration to sqlalchemy 2.0 
new ORM usage (deprecating the legacy Query API).

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
from typing import Optional

from flask import request
from flask import url_for
from flask.views import MethodView

from automua.database import populate_db
from automua.database import purge_db
from automua.model import Provider
from automua.model import db

from sqlalchemy import func, select

class InitDatabase(MethodView):
    """Initialise database."""

    @staticmethod
    def _response(msg) -> str:
        url = url_for('root')
        return f'<html><body>{msg}. <a href="{url}">Click here</a> to go back.</body></html>'

    def init_db(self, data: Optional[dict]) -> str:
        db.create_all()
        pid = db.session.scalar(select(func.count()).select_from(Provider))
        if pid == 0:
            populate_db(data)
            db.session.commit()
            m = 'Database is now prepared'
        else:  # pragma: no cover
            m = 'Database already contains provider data'
        return self._response(m)

    def delete(self):
        purge_db()
        return self._response('Database content purged')

    def get(self):
        return self.init_db(None)

    def post(self):
        return self.init_db(request.json)
