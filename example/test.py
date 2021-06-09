import json
import sys
import dtt
from dtt import DictToTable
sys.setrecursionlimit(10000)
my_file = open("test", "r")

json1_data = json.loads(my_file.read())

dttb = DictToTable(json1_data)

print(dttb.create_ddl_string("sSTATIONS"))

print(json1_data)