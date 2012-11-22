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

import tldap
import tldap.base
import tldap.fields

# Active Directory

class user(tldap.base.LDAPobject):
    displayName = tldap.fields.CharField()
    givenName = tldap.fields.CharField()
    loginShell = tldap.fields.CharField()
    mail = tldap.fields.CharField()
    memberOf = tldap.fields.CharField(max_instances=None)
    objectSid = tldap.fields.SidField()
    o = tldap.fields.CharField()
    sAMAccountName = tldap.fields.CharField(required=True)
    sn = tldap.fields.CharField()
    telephoneNumber = tldap.fields.CharField()
    title = tldap.fields.CharField()
    unicodePwd = tldap.fields.CharField()
    unixHomeDirectory = tldap.fields.CharField()
    userAccountControl = tldap.fields.IntegerField()

    class Meta:
        object_classes = { 'user', }

class group(tldap.base.LDAPobject):
    cn = tldap.fields.CharField()
    displayName = tldap.fields.CharField()
    gidNumber = tldap.fields.IntegerField()
    member = tldap.fields.CharField(max_instances=None)
    objectSid = tldap.fields.SidField()
    sAMAccountName = tldap.fields.CharField()

    class Meta:
        object_classes = { 'group', }

