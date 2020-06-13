import re

for line in open('db_creation_script.sql'):
    statement = ""
    if re.match(r'^--', line):
        continue
    if not re.search(r';$', line):
        statement = statement + line
    else:
        statement = statement + line
        print(statement)
        statement = ""
