import os
import json
from json import dumps # used later on (load)
import string

from .config import *
# import text for easier text output changes

class Database:
    def __init__(self) -> None:
        """
        Select the save method for the "Database", currently only json file is an option to save
        more databases will be added later
        txt will be the next method added
        """

    class normal: # normal version | the version you should use if you have already experience with databases like mysql, mariadb, sqlite, etc
        def __init__(self, db_path=db_folder_normal) -> None:
            self.path = db_path
            self.save_method = "json"
            self.json_indent = 4

            if self.save_method == "json":
                if not os.path.exists(self.path):
                    os.mkdir(self.path) # creates path for databases 

        def read_db(self, database: str) -> dict:
            if self.save_method == "json":
                with open(f"{self.path}{database}", "r") as json_file:
                    data = json.load(json_file)
                    return data


        def overwrite_db(self, database: str, data: dict) -> None:
            if self.save_method == "json":
                with open(f"{self.path}{database}", "w") as json_file:
                    json_file.write(dumps(data, indent=self.json_indent))
                    return


        def read_structure(self, database: str, table: str) -> dict:
            if self.save_method == "json":
                data = self.read_db(database)
                table_structure = data[table]["0"]
                return table_structure


        def list_databases(self) -> list:
            if self.save_method == "json":
                data = os.listdir(self.path)
                db_list = []
                for db in data:
                    name, _ = db.split(".")
                    db_list.append(name)
                return db_list


        def list_tables(self, database: str) -> list:
            """
            lists all tables in a database
            """
            if self.save_method == "json":
                data = self.read_db(database)
                table_list = list(data)
                return table_list


        def next_table_row(self, database: str, table: str) -> int:
            if self.save_method == "json":
                table_data = self.read_db(database)[table]
                number_list = list(table_data)
                num = 1

                while True:
                    if not str(num) in number_list:
                        break
                    else:
                        num += 1

                return num


        def create_database(self, database: str) -> int | str:
            """
            database:  is the name of the new database
            """
            if self.save_method == "json":
                db_list = self.list_databases()

                if database in db_list:
                    return 401, "Database already exists"
                elif r"!#$%&'()*+,-./:;<=>?@[\]^`{|}~" in database or '"' in database:
                    return 401, "Only numbers, letters and underscores are allowed" 
                else:
                    with open(f"{self.path}/{database}.json", "w") as f:
                        f.write(dumps({}, indent=self.json_indent))

                    return 200, "Created Database"


        def drop_database(self, db_name :str) -> int | str:
            db_list = self.list_databases()

            if not db_name in db_list:
                return 401, "Database doesnt exist"

            os.remove(f"{self.path}/{db_name}.json")
            return 200,  "Database deleted"


        def create_table(self, database: str, tablename: str, structure: list) -> str | bool:
            """
            tablename
            structure is built with two string and one seperator "::"
            z.b. ["username::str", "age::int"] types allowed:"str, int"
            """
            if self.save_method == "json":
                data = self.read_db(database)
                table_list = self.list_tables(database)

                for table in table_list:
                    if table == tablename:
                        return "Tablename is already in use"

                structure_list = {}

                for struc in structure:
                    try:
                        struc_name, struc_type = str(struc).split("::")
                    except:
                        return "Something went wrong in your structure. Maybe forgot to use the seperator '::' between the name and the type"
                    if not struc_type in ["str", "int"]:
                        return "Invalid type"

                    structure_list[struc_name] = struc_type

                data[tablename] = {"0": structure_list}
                
                # saves it to file
                self.overwrite_db(database, data)
                return True
        

        def drop_table(self, database:str,  tablename: str) -> str:
            if self.save_method == "json":
                data = self.read_db(database)
                table_list = self.list_tables(database)
                if tablename in table_list:
                    data.pop(tablename)

                    self.overwrite_db(database, data)
                return "Table doesnt exist"


        def rename_table(self, database: str, tablename: str, new_name: str):
            if self.save_method == "json":
                data = self.read_db(database)
                try: # checks if tablename exists
                    table = data[tablename]
                except:
                    return "Table couldnt be found"
                
                table_list = self.list_tables(database) # checks if new_name is already in use
                if new_name in table_list:
                    return f"The name you want to give '{tablename}' is already in use"

                data[new_name] = table

                self.overwrite_db(database, data)

                print(self.drop_table(database, tablename))

                return True


        def insert_into_table(self, database: str, tablename: str, value: dict) -> str | bool:
            """
            insert into table | value example {"name": "examplename", "username": "exampleusername"}
            """
            if self.save_method == "json": # remove func and replace it with a normal dict and at the end of insert func overwrite json file
                if not tablename in self.list_tables(database): 
                    return "Tablename is not in use"

                if value == {}:
                    return "Add something to the value dictionary"

                try:
                    data = self.read_db(database)
                except:
                    return "Your file is corrupt"
                #table = data[tablename] # initialies the table data

                try:
                    structure = self.read_structure(database, tablename) # reads the structure of the table
                    # gets the names of the structure
                except:
                    return "Structure doesnt exist in this table ???"

                content_list = {}

                for struc in structure:
                    for value_ in value:
                        content = value[value_] # content to save

                        if str(value_) == struc: # checks if content is the same as the structure list
                            if structure[struc] == "str":
                                if type(content) == str:
                                    content_list[value_] = content
                                else:
                                    return "You got the wrong name or wrong data type"
                            elif structure[struc] == "int":
                                if type(content) == int:
                                    content_list[value_] = content
                                else:
                                    return "You got the wrong name or wrong data type"

                print(content_list)
                number = self.next_table_row(database, tablename)
                data[tablename][number] = content_list

                self.overwrite_db(database, data)
                return True


        def drop_row_by_number(self, database: str, tablename: str, row: int):
                if self.save_method == "json":
                    data = self.read_db(database)
                    try:
                        data = data[tablename]
                    except:
                        pass

                    if row == 0:
                        return "You cant drop row 0 (stores the structure of the table)"
                    
                    data.pop(str(row))

                    self.overwrite_db(database, data)

                    return True


        def use_sql_lang(self, code: str, sql_terminal=False):
            # translates the sql language and creates everything

            words = str(code).lower()
            words = str(words).split()
            
            try:
                if words[0] == "select": # you have to use use command before or select a db before
                    if words[1] == "*":
                        if words[2] == "from":
                            table = words[3]
                    else:
                        column_name = words[1]
                elif words[0] == "update":
                    pass
                elif words[0] == "delete":
                    pass
                elif words[0] == "insert":
                    pass # into


                elif words[0] == "create":
                    if words[1] == "database":
                        return self.create_database(words[2])
                    elif words[1] == "table":
                        pass
                    elif words[1] == "index":
                        pass
                elif words[0] == "alter":
                    if words[1] == "database":
                        pass
                    elif words[1] == "table":
                        pass
                    elif words[1] == "index":
                        pass
                elif words[0] == "drop":
                    if words[1] == "database":
                        return self.drop_database(words[2])
                    elif words[1] == "table":
                        pass
                    elif words[1] == "index":
                        pass
                elif words[0] == "use": # sql_terminal command only
                    try:
                        word1 = words[1]
                    except:
                        if sql_terminal:
                            return "use", None
                        else:
                            return "This is a command for the sql_terminal"

                    if words[1] in self.list_databases():
                        if word1 == "none":
                            word1 = None

                        if sql_terminal:
                            return "use", word1
                        else:
                            return "This is a command for the sql_terminal"
                    else:
                        if sql_terminal:
                            return "DatabaseError: Database doesnt exist"
                        else:
                            return "This is a command for the sql_terminal"
                            
                

                else:
                    return "No Command"
            except Exception as e:
                return 401, "You dindnt gave enough arguments", e
                

        def sql_terminal(self):
            current_database = None
            while True:
                code = input(f"DB_NAME [{current_database}]> ")

                if not code == "":
                    response = self.use_sql_lang(code=code, sql_terminal=True)
                    
                    if type(response) == list or type(response) == tuple:
                        if response[0] == "use":
                            current_database = response[1]
                    else:
                        print(response)
                




#elif words[1] == "user": # maybe ill create a user func (which is save) but if then at the end

    
    class simple: # create a second version wich is simplified (lightweight) inspirated by replits builtin database (keystorage)
        """
        NOT USABLE
        """
        def __init__(self, db_folder=db_folder_simple) -> None:
            self.db_folder = db_folder
            
            self.save_method = "json"
            self.json_indent = 4

            #if self.save_method == "json":
            #    if not os.path.exists(self.db_path):

            #        open(self.db_path, "w").write(dumps({}, indent=self.json_indent))

        def setkeytovalue(self, key, value):
            """
            # Set a key to a value
            """
            # file = self.readfiel()
            

        def getkeysvalue(self, key):
            """
            # Get a key's value
            """
            #return value

        def deletekey(self, key):
            """
            # Delete a key
            """


        def listkeys(self):
            """
            # List all keys
            """

        
        def listkeywithprefix(self, prefix):
            """
            # Search for a key/s
        """

    #def create_table(self, tablename):
    #    PATH = f"{DATABASE_DIRECTORY}/{tablename}.txt"
    #
    #    if os.path.exists(PATH):
    #        return "Table already exists"

    #    open(PATH) # creates file

    #    with open(f"{DATABASE_DIRECTORY}/tables.txt") as w:
    #        w.write(f"{tablename}\n")
    #        w.close()
        
    #    return "Table created successfully"

    
    #def list_tables(self):
    #    with open(f"{DATABASE_DIRECTORY}/tables.txt") as w:
    #        table_list = []
    #        for table in w.readlines():
    #            table_list.append(table)
    #        w.close()
    #        return table_list


    #def add(self, key, value):
    #    pass# problem how to save more then one key 
        # create a database in python you can access over http request and 
        # local request with user etc, and select in what file to save it