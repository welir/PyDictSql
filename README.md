# PyDyctSql
Python str dict to sql DDl Table converter

EXAMPLE USAGE

      import dtt
      you_dict = {}
      
      you_dict["A"] = '99'
      you_dict["B"] = 'b'
      you_dict["C"] = '1.1'
      you_dict["D"] = '2018-01-01 10:10:10'

      st_db = dtt.DictToTable(you_dict)
      ddl_str = st_db.create_ddl_string('TEST')

      print(ddl_str)

RESULT

  create table TEST (
  A smallint,
  B varchar(512),
  C decimal,
  D datetime2(7));
