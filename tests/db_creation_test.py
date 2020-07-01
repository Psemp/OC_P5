import re


def DatabaseCreation(cursor):
    with open('db_script_test.sql', 'r') as sql:
        statement = ""

        for line in sql:
            if re.findall("^-- ", line):
                continue
            if len(line) == 0:
                continue
            if not re.search(";$", line):
                statement = statement + line
            else:
                statement = statement + line
                cursor.execute(statement)
                statement = ""
