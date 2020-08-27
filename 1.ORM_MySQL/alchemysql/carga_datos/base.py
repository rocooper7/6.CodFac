from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:Cooperboy0071985@localhost/mysql7', echo=False) 

Session = sessionmaker(bind=engine)

Base = declarative_base()




