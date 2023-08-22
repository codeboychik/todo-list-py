import csv

table_name = 'person'

with open('../data/data.csv') as file:
    content = list(csv.reader(file))

column_names = ",".join(item for item in content[0])

inserts = [f"INSERT INTO {table_name}({column_names}) VALUES({','.join(val for val in item)})\n"
           for item in content[1:]]

with open('../data/result.sql', 'w') as file:
    file.writelines(inserts)
