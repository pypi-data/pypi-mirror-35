#! /usr/bin/env python
# coding: utf-8
import sys
import argparse
from ldap_user import LDAPConfig

__author__ = '鹛桑够'


def create_config():
    args_man = argparse.ArgumentParser()
    args_man.add_argument("--admin-user", dest="admin_user", metavar="user_name", help="LDAP admin user", required=True)
    args_man.add_argument("--admin-password", dest="admin_password", metavar="password", help="LDAP adim user password",
                          required=True)
    args_man.add_argument("config_path", metavar="path", nargs="?", help="where to save. default is stdout.")
    if len(sys.argv) <= 1:
        sys.argv.append("-h")
    args = args_man.parse_args()
    LDAPConfig.create(args.config_path, admin_user=args.admin_user, admin_password=args.admin_password)

if __name__ == "__main__":

    create_config()
