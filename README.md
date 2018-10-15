# PyDyctSql
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
