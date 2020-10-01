# PyDictSql
Python str dict to sql DDl Table converter

EXAMPLE USAGE

      import dtt
      
      //example dict
      you_dict = {}
      
      you_dict["A"] = '99'
      you_dict["B"] = 'b'
      you_dict["C"] = '1.1'
      you_dict["D"] = '2018-01-01 10:10:10'

      // create class
      st_db = dtt.DictToTable(you_dict) // input you dict, where all values is str
      
      // convert to ddl
      ddl_str = st_db.create_ddl_string('TEST') // input you table name

      print(ddl_str)

RESULT

  create table TEST (
  A smallint,
  B varchar(512),
  C decimal,
  D datetime2(7));


ANOTHER EXAMPLE USAGE
      d1 = {}  # to make a dictionary
print(type(d1))  # to print a dictionary
d2 = {"Alex": "Fried rice", "Karen": "Noodles", "Sarah": "Burger",
      "Sherlock": {"b": "Manchurian", "l": "Rice", "d": "Chicken"}}  # to make another dictionary
d2["Andrew"] = "Junk food"  # to add keys and items
d2[452] = "Barbeques"  # to add keys and items
del d2[452]  # to remove keys and items
print(d2)  # to print second dictionary
d3 = d2.copy()  # to make a copy and new dictionary of d2
del d3["Alex"]  # to remove keys and items
print(d3)  # to print the third dictionary
d2.update({"Rock": "Candies"})  # to add keys and items-second method
print(d2.items())  # to print the items only
print(d2.keys())  # to print the keys only
