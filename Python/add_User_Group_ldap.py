#!/usr/bin/python

# import class and constants
from ldap3 import Server, Connection, ALL
import yaml
import sys


# Importing test data from YAML config file
with open("data.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# Declaring variables and assigning the values from YAML config file
server_uri = cfg['server']['server_uri']
admin_user = cfg['connection']['admin_user']
admin_password = cfg['connection']['password']
user_base = cfg['user']['user_base']
user_attrs = cfg['user']['attributes']
group_base = cfg['group']['group_base']
group_attrs = cfg['group']['attributes']
	
# Defining function to add a ldap user
def add_ldap_user():
    # define the server
    server = Server(server_uri, get_info=ALL)
	# define the connection
    conn = Connection(server, user=admin_user, password=admin_password, auto_bind=True)
    # perform the Add operation to add an user
    conn.add(user_base, attributes=user_attrs)
    print(conn.result)
    # close the connection
    conn.unbind()

# Defining function to add a ldap group
def add_ldap_group():
    # define the server
    server = Server(server_uri, get_info=ALL)
	# define the connection
    conn = Connection(server, user=admin_user, password=admin_password, auto_bind=True)
    # perform the Add operation to add a group
    conn.add(group_base, attributes=group_attrs)
    print(conn.result)
    # close the connection
    conn.unbind()

add_ldap_user()
add_ldap_group()
    