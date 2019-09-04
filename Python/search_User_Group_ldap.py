#!/usr/bin/python
	
# import class and constants
from ldap3 import Server, \
    Connection, \
    SUBTREE, \
    ALL_ATTRIBUTES, \
	ALL
import yaml
import sys


# Importing test data from YAML config file
with open("data.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
	
# Declaring variables and assigning the values from YAML config file
server_uri = cfg['server']['server_uri']
search_base = cfg['server']['search_base']
attrs = ALL_ATTRIBUTES
 
# Defining Search User or Group function 
def get_user_group_info(cn):
    server = Server(server_uri)
    with Connection(server, auto_bind=True) as conn:
        conn.search(search_base, search_filter='(cn=' + cn + ')', 
		            search_scope=SUBTREE, attributes=attrs,
					get_operational_attributes=True)
    print(conn.entries)
    print(conn.result)

# Calling Search User or Group method 	
get_user_group_info(sys.argv[1])
