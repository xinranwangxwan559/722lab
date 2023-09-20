# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:27:22 2023

@author: chris
"""

import mysql.connector
myconn = mysql.connector.connect(
    host='localhost',
    port = 3306,
    user = 'root',
    password = 'WANGyu1219',
    database = 'world')

mycursor = myconn.cursor()

mycursor.execute('SELECT * FROM world.country')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
import pandas as pd

sql = 'select * from country where continent= "Oceania"'

df = pd.read_sql_query(sql,myconn)

from sqlalchemy import create_engine

myengine = create_engine("mysql+mysqlconnector://root:WANGyu1219@localhost:3306/world")
df = pd.read_sql_table('country', myengine)