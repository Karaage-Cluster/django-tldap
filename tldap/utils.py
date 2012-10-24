# Copyright 2012 VPAC
#
# This file is part of django-tldap.
#
# django-tldap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-tldap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django-tldap  If not, see <http://www.gnu.org/licenses/>.

import sys

DEFAULT_LDAP_ALIAS = "default"

def load_backend(backend_name):
    __import__(backend_name)
    return sys.modules[backend_name]

class ConnectionHandler(object):
    def __init__(self, databases):
        self.databases = databases
        self._connections = {}

    def __getitem__(self, alias):
        if alias in self._connections:
            return self._connections[alias]

        db = self.databases[alias]

        backend = load_backend(db['ENGINE'])
        conn = backend.LDAPwrapper(db)
        self._connections[alias] = conn
        return conn

    def __iter__(self):
        return iter(self.databases)

    def all(self):
        return [self[alias] for alias in self]

