import pymysql.cursors
import pymysql
import pandas as pd
import numpy as np
import json
import argparse
import warnings
warnings.filterwarnings('ignore')
try:
    def Startup(source_dir, mysql_details, destination_table,):
        conn = pymysql.connect(host=mysql_details['my_sql'],database=mysql_details['database'],user=mysql_details['username'],password=mysql_details['password'])
        print("Connection success")
        with conn.cursor() as cursor:
            cursor.execute("select database();")
            records = cursor.fetchone()
            print(" Connected to database: ", records)
            print('Creating table....')
            
            cursor.execute(destination_table)
            print("Table is created....")
            
            for i,row in source_dir.iterrows():
                sql = "INSERT INTO startup.startup VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                conn.commit()
            print("All records Successfully inserted")
except Exception as err:
    print("Connection Failed!!")
    print(err)
parser = argparse.ArgumentParser(description='Json file')
parser.add_argument('--json',help='Json file link')
args = parser.parse_args()
v1 = vars(args)
with open(args.json) as a:
    mysql_details = json.load(a)
    print(mysql_details)
StartupData = pd.read_csv("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\startup.csv")
StartupData['Amount_in_USD'] = StartupData['Amount_in_USD'].str.replace(',','')
StartupData['Amount_in_USD'] = StartupData['Amount_in_USD'].replace(np.nan,0)
StartupData['Date'] = StartupData['Date'].str.replace('/','-')
StartupData['Date'] = StartupData['Date'].str.replace('.','-')
StartupData = StartupData.replace(np.nan, 0)
destination_table ="CREATE TABLE if not exists startup(Sr_No int primary key,Date varchar(50),Startup_Name varchar(255),Industry_Vertical varchar(255),SubVertical varchar(255),City varchar(255),Investors_Name varchar(255),InvestmentnType varchar(255),Amount_in_USD text,Remarks varchar(255))"
Startup(StartupData,mysql_details,destination_table)


