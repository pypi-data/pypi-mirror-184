import __init__ as db

db = db.Database.normal()

#print(db.create_table("test", ["name::str", "username::str"]))

#print(db.read_structure("NEXT_FORMAT"))

#print(db.insert_into_table("test", {"name": "testname", "username": "testusername"}))

#print(db.next_number_to_use("NEXT_FORMAT"))

#print(db.drop_table("test"))

#print(db.drop_row_by_number("test", 1))

#print(db.read_structure("test"))

#print(db.rename_table("table2", "table4"))

#print(db.use_sql_lang("create database"))

#print(db.create_database("dsdasda"))

#print(db.drop_database("dsa"))

#print(db.list_databases())

db.sql_terminal()