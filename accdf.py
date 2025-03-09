import streamlit as st
import pyodbc
import pandas as pd
#import sqlalchemy as sa


#cnxn   = pyodbc.connect(...)
    
...
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=C:\iqra\mfa.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
for row in cursor.tables():    #ok
    print (row.table_name)    #ok
    st.write(row.table_name)    #ok



#table_name = 'DB_IMPORT_2020_PM'

#engine = sa.create_engine("access+pyodbc://@my_accdb_dsn")
#df = pd.read_sql_table(table_name, engine)
#print(df)

query = "SELECT * FROM Payments"
dataf = pd.read_sql(query, conn)
conn.close()
#print(dataf)
st.dataframe(dataf) 

