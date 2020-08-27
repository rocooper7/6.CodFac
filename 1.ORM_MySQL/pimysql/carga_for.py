import pymysql
import pandas as pd

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',  #ip
            user = 'root',
            password = 'Cooperboy0071985',
            db = 'mysql7'
        )
        self.cursor = self.connection.cursor()
        print('Conexión Establecida')

    def carga(self):
        df = pd.read_csv('C:\Absenteeism_predictions.csv')
        insert_query = 'INSERT INTO predicted_outputs VALUES'
        
        for i in range(df.shape[0]):
            insert_query += '(' 
            
            for j in range(df.shape[1]):
                insert_query += str(df[df.columns.values[j]][i]) + ', '
    
            insert_query = insert_query[:-2] + '), ' 

        insert_query = insert_query[:-2] + ';'
        print(insert_query)        
        try:
            self.cursor.execute(insert_query)
        except Exception as e:
            raise
        self.connection.commit()
        self.connection.close()

if __name__ == '__main__':
    database = DataBase()
    database.carga()