import sqlite3
import pandas as pd 

#Initilize db connection, staff.db is db_name, which will be created if no existing found
connection = sqlite3.connect('STAFF.db')

#initialize table parameter if necessary(here our data did not had column name so we initialize them)
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', "LNAME", 'CITY', 'CCODE']

#read csv as a dataframe
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

#add df as table to database
df.to_sql(table_name, connection, if_exists = 'replace', index = False)
print('Table is ready')

#query the table
query_statement = f'Select * from {table_name}'
query_output = pd.read_sql(query_statement, connection)
print(query_statement)
print(query_output)

query_statement = f'select fname from {table_name}'
query_output = pd.read_sql(query_statement, connection)
print(query_statement)
print(query_output)

query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, connection)
print(query_statement)
print(query_output)

#create new row to insert in table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
#conver dict to dataframe
data_append = pd.DataFrame(data_dict)

#append row to INSTRUCTOR table 
data_append.to_sql(table_name, connection, if_exists = "append", index = False)
print('Data appended successfully')

# the new count should now have one more data
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, connection)
print(query_statement)
print(query_output)

#close database connection
connection.close()



