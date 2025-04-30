#This python script creates a database and populates it with tables.
#If the tables already exist, they are dropped and re-created.

import sqlite3

connection = sqlite3.connect('sports_fixtures.db')
connection.row_factory = sqlite3.Row

query = 'DROP TABLE If EXISTS Location;'
result = connection.execute(query)

query = 'CREATE TABLE Location (LocationID INTEGER PRIMARY KEY,Location varchar(255),Address varchar(255));'
result = connection.execute(query)

query = "INSERT INTO Location (Location,Address) VALUES ('Cranbrook Junior School','5 Victoria Road, Bellevue Hill');"
result = connection.execute(query)

query = "INSERT INTO Location (Location,Address) VALUES ('Lyne Park','600 New South Head Rd, Rose Bay NSW 2029');"
result = connection.execute(query)

query = "INSERT INTO Location (Location,Address) VALUES ('Knox Grammar School','2 Borambil Street, Wahroonga');"
result = connection.execute(query)

query = "INSERT INTO Location (Location,Address) VALUES ('Trinity Grammar School','119 Prospect Road, Summer Hill, NSW, 2130');"
result = connection.execute(query)

connection.commit()

query = 'DROP TABLE If EXISTS Sports_Transport;'
result = connection.execute(query)

query = 'CREATE TABLE Sports_Transport (StudentName varchar(255) PRIMARY KEY, Location int, Drop_off varchar(7), Pick_up varchar(7), Date varchar(8), MOD int);'
result = connection.execute(query)

transportlist =[
    ["Steven.K", 4, "9:00am", "2:00pm", "25/02/25", 3],
    ["James.M", 3, "11:30am", "1:20pm", "25/02/25", 2],
    ["Tom.C", 1, "10:05am", "2:50pm", "25/02/25", 5],
    ["Hugo.M", 2, "8:30am", "12:00pm", "25/02/25", 1]
]

query = "INSERT INTO Sports_Transport (StudentName, Location , Drop_off , Pick_up, Date , MOD) VALUES "
firstitem = True
for Student in transportlist:
    if not firstitem:
        query = query + ", "
    query = query + '("{}",{},"{}","{}","{}",{})'.format(Student[0], Student[1], Student[2], Student[3], Student[4], Student[5])
    firstitem = False
query = query + ";"

result = connection.execute(query)

connection.commit()

query = 'DROP TABLE If EXISTS MOD;'
result = connection.execute(query)

query = 'CREATE TABLE MOD (MODID INTEGER PRIMARY KEY, Name varchar(50));'
result = connection.execute(query)

MODlist =[
    ["Josh"],
    ["Kitty"],
    ["Uncles"],
    ["Bev"],
    ["Ms Witten"],
    ["Smith"],
]

query = "INSERT INTO MOD (Name) VALUES "
firstitem = True
for MOD in MODlist:
    if not firstitem:
        query = query + ", "
    query = query + '("{}")'.format(MOD[0])
    firstitem = False
query = query + ";"

result = connection.execute(query)

connection.commit()

