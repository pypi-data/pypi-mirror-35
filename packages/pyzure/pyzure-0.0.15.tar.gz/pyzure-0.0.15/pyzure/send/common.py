import pyzure
from pyzure.connection.connection import connect
from pyzure.tools.print_colors import C


def cleaning_function(instance, table_name, dev=False):
    print("Get info on table...")
    columns = get_table_info(instance, table_name)
    print("Get info on table...OK")
    cnxn = connect(instance)
    cursor = cnxn.cursor()
    drop_request = '''DROP TABLE ''' + table_name + ''';'''
    print(C.WARNING + "Drop table " + C.ENDC)
    cursor.execute(drop_request)
    cnxn.commit()
    cursor.close()
    cnxn.close()
    print("Create table from info...")
    create_table_from_info(instance, columns, table_name)
    print("Create table from info...OK")
    print(C.OKBLUE + "Cleaning Done" + C.ENDC)
    return 0


def get_table_info(instance, table_and_schema_name):
    split = table_and_schema_name.split(".")
    if len(split) == 1:
        table_name = split[0]
        schema_name = None

    elif len(split) == 2:
        table_name = split[1]
        schema_name = split[0]
    else:
        raise Exception("Invalid table or schema name")
    query = "SELECT column_name, data_type, character_maximum_length, is_nullable FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='%s'" % table_name
    if schema_name:
        query = query + " AND TABLE_SCHEMA='%s'" % schema_name
    print(query)
    return pyzure.execute_query(instance, query)


def create_table_from_info(instance, columns, table_name):
    columns_name_string = []
    for c in columns:
        # COLUMN NAME
        c_string = c["column_name"]

        # DATA TYPE TREATMENT
        data_type = c["data_type"]
        if data_type in ("varchar"):
            data_type = data_type + "(" + str(c["character_maximum_length"]) + ")"

        c_string = c_string + " " + data_type

        # NULLABLE ?
        if c["is_nullable"] == "NO":
            c_string = c_string + " NOT NULL"

        columns_name_string.append(c_string)

    query = "CREATE TABLE %s (%s)" % (table_name, ", ".join(columns_name_string))
    print(query)
    pyzure.execute_query(instance, query)


def commit_function(cnxn):
    cnxn.commit()
    print(C.OKGREEN + "Committed" + C.ENDC)
