import pandas as pd
from sqlalchemy import create_engine

db_uri = 'mysql+pymysql://root:Cooperboy0071985@localhost/mysql7'

engine = create_engine(db_uri, echo=False) # enter your password and database names here

df = pd.read_csv('C:\Absenteeism_predictions2.csv',sep=',',quotechar='\'',encoding='utf8')

print(df)

sample_sql_database = df.to_sql('sample_database3', con=engine,index=False,if_exists='append')

sample_sql_database = engine.execute("SELECT * FROM sample_database3").fetchall()

print(sample_sql_database)

#df.to_sql('Table_name',con=engine,index=False,if_exists='append') # Replace Table_name with your sql table name
