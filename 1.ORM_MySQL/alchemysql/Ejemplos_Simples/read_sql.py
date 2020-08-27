from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:Cooperboy0071985@localhost/mysql7', echo=False) 

conn = engine.connect()

sql = 'select * from sample_database'
df = pd.read_sql(sql, conn)
print(df)

#df2 = pd.read_sql_query("Select * from Album",engine)