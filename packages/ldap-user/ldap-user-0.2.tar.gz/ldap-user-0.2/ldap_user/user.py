#! /usr/bin/env python
# coding: utf-8

import os
import re
import datetime
import ldap
from ldap import SCOPE_SUBTREE as LDAP_SCOPE_SUBTREE
from ldap import modlist, LDAPError
from ldap_user.util.verify_secret import verify, SUPPORT_METHOD

__author__ = '鹛桑够'


class LDAPUser(object):

    EPOCH_DATE = datetime.datetime.fromtimestamp(0)
    LOGIN_SHELL = "/bin/bash"
    HOME_BASE_DIRECTORY = "/home"
    GROUP_ID_NUMBER = None
    CREATOR = None

    password_compile = re.compile("^{(%s)}(\S+)$" % "|".join(SUPPORT_METHOD))

    def __init__(self, ldap_uri, base_dn, admin_user, admin_password, home_base_directory=None, group_id=None):
        self.ldap_com = ldap.initialize(ldap_uri)
        self.ldap_base_dn = base_dn
        if home_base_directory is not None:
            self.HOME_BASE_DIRECTORY = home_base_directory
        if group_id is not None:
            self.GROUP_ID_NUMBER = "%s" % group_id
        self.ldap_admin = "cn=%s,%s" % (admin_user, self.ldap_base_dn)
        self.people_base_cn = "ou=People,%s" % self.ldap_base_dn
        self.ldap_com.bind_s(self.ldap_admin, admin_password)

    def __get_next_uid_number(self):
        filter_str = "uid=*"
        attributes = ["uidNumber", "gidNumber"]
        items = self.ldap_com.search_s(self.people_base_cn, LDAP_SCOPE_SUBTREE, filter_str, attributes)
        max_number = 1000
        for item in items:
            print(item)
            if "uidNumber" in item[1]:
                u_number = int(item[1]["uidNumber"][0])
                if max_number < u_number:
                    max_number = u_number
        return max_number + 1

    def delete_user(self, user_name):
        if self.exist(user_name) is None:
            return True
        dn = "uid=%s,%s" % (user_name, self.people_base_cn)
        return self.ldap_com.delete_s(dn)

    def add_user(self, user_name, uid_number=None, gid_number=None, home_directory=None):
        dn = "uid=%s,%s" % (user_name, self.people_base_cn)
        attributes = dict()
        for key in ("uid", "cn", "sn"):
            attributes[key] = user_name
        attributes["objectClass"] = ["top", "person", "inetOrgPerson", "posixAccount", "organizationalPerson",
                                     "shadowAccount"]
        if uid_number is None:
            attributes["uidNumber"] = "%s" % self.__get_next_uid_number()
        else:
            attributes["uidNumber"] = uid_number
        if gid_number is None:
            attributes["gidNumber"] = self.GROUP_ID_NUMBER
        else:
            attributes["gidNumber"] = "%s" % gid_number
        if attributes["gidNumber"] is None:
            raise LDAPError("please set gidNumber")
        if home_directory is None:
            home_directory = os.path.join(self.HOME_BASE_DIRECTORY, user_name)
        attributes["homeDirectory"] = home_directory
        attributes["loginShell"] = self.LOGIN_SHELL
        print(attributes)
        if self.CREATOR is not None:
            attributes["givenName"] = self.CREATOR
        mod_list = ldap.modlist.addModlist(attributes)
        self.ldap_com.add_s(dn, mod_list)

    def expire_user(self, user_name, shadow_expire=None):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        old_attributes = user_entry[1]
        attributes = dict(**old_attributes)
        if shadow_expire is None:
            attributes["shadowExpire"] = ["%s" % (datetime.datetime.now() - self.EPOCH_DATE).days]
        else:
            attributes["shadowExpire"] = ""
        mod_list = ldap.modlist.modifyModlist(old_attributes, attributes)
        return self.ldap_com.modify_s(user_entry[0], mod_list)

    def block_user(self, user_name):
        return self.expire_user(user_name)

    def unlock_user(self, user_name):
        return self.expire_user(user_name, "")

    def exist(self, user_name, *attributes):
        l_attributes = set(attributes)
        # l_attributes.add("userPassword")
        # l_attributes.add("shadowExpire")
        sr = self.ldap_com.search_s(self.ldap_base_dn, LDAP_SCOPE_SUBTREE, "uid=%s" % user_name, l_attributes)
        if len(sr) <= 0:
            return None
        return sr[0]

    def verify_password(self, password, ldap_password):
        match_r = self.password_compile.match(ldap_password)
        if match_r is not None:
            method = match_r.groups()[0]
            cipher_text = match_r.groups()[1]
            return verify(method, password, cipher_text)
        return password == ldap_password

    def login(self, user_name, password):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        attr = user_entry[1]
        if "userPassword" not in attr:
            return False

        ldap_password = attr["userPassword"][0]
        return self.verify_password(password, ldap_password)

    def set_password(self, user_name, new_password):
        user_entry = self.exist(user_name)
        if user_entry is None:
            return False
        pr = self.ldap_com.passwd_s(user_entry[0], None, new_password)
        if pr[0] is None and pr[1] is None:
            return True
        return False

