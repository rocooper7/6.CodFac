import pymysql

class DataBase:
    def __init__(self):
        self.db_name = None
        self.connection = pymysql.connect(
            host = 'localhost',  #ip
            user = 'root',
            password = 'Cooperboy0071985',
            db = self.db_name
        )
        self.cursor = self.connection.cursor()
        print('Conexión Establecida')
    
    
    def create_database(self,db_name):
        create_db = f'CREATE DATABASE {db_name}'
        try:
            self.cursor.execute(create_db)
            print('New Database has been created')
        except Exception as e:
            raise


    def drop_database(self,db_name):
        drop_db = f'DROP DATABASE {db_name}'
        try:
            self.cursor.execute(drop_db)  
            print(f'Database {db_name} deleted')
        except Exception as e:
            raise


    def show_database(self):
        show_db = f'SHOW DATABASES'
        try:
            self.cursor.execute(show_db)
            databases = self.cursor.fetchall()
            for database in databases:
                print ('Databases:', database[0])
        except Exception as e:
            raise


    def use_database(self,db_name):    
        use_db = f'USE {db_name}'
        try:
            self.cursor.execute(use_db)
            self.connection.commit()
            self.db_name = db_name
            print(f'Using {db_name} database')
        except Exception as e:
            raise


    def create_table(self,table_name):
        drop_table = f"DROP TABLE IF EXISTS {table_name}"
        create_table = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(50), password VARCHAR(50))"
        try: 
            self.cursor.execute(drop_table)
            print('Existing table has been deleted')
            self.cursor.execute(create_table)
            print('New table has been created')
        except Exception as e:
            raise
   
   
    def show_table(self):
        show_tables = 'SHOW TABLES'
        try:
            self.cursor.execute(show_tables)
            tables = self.cursor.fetchall()
            for table in tables:
                print(table)
        except Exception as e:
            raise


    def insert_info(self,table_name):
        insert_query = f'INSERT INTO {table_name} (username,password) VALUES (%s,%s)'
        val = [('Peter', 'Lowstreet'),
        ('Amy', 'Apple'),
        ('Hannah', 'Mountain'),
        ('Michael', 'Valley'),
        ('Sandy', 'Oceanblvd'),
        ('Betty', 'GreenGrass'),
        ('Richard', 'Sky'),
        ('Susan', 'One'),
        ('Vicky', 'Yellow'),
        ('Ben', 'ParK'),
        ('William', 'Central'),
        ('Chuck', 'Main'),
        ('Viola', 'Sideway')]

        try:
            self.cursor.executemany(insert_query,val)
            self.connection.commit()
            print('Data has been insert')
        except Exception as e:
            self.connection.rollback()


    def select_user(self,id):
        sql = f'SELECT * FROM dbpython WHERE id = {id}'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            
            for user in users:
                print(user)    
                print('ID:', user[0])
                print('Username:', user[1])
                print('Password:', user[2])

        except Exception  as e:
            raise
  

    def update_user(self,id,username,password):
        sql = f"UPDATE dbpython SET username ='{username}',password = '{password}' WHERE id = {id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()      
            print('Updated user,done')       
        except Exception as e:
            self.connection.rollback() 


    def delete_user(self,id):
        sql = f'DELETE FROM dbpython WHERE id = {id}'
        try:
            self.cursor.execute(sql)
            self.connection.commit()      
            print('Delete user,done')       
        except Exception as e:
            self.connection.rollback() 


    def close(self):
        self.connection.close()



if __name__ == '__main__':
    database = DataBase()
    #database.create_database('python')
    #database.drop_database('python')
    #database.show_database()
    database.use_database('dbpython')
    #database.select_user(1)
    database.update_user(2,'Salvador','Cooper')
    #database.delete_user(13)
    #database.select_user(1)
    #database.create_table('dbpython')
    #database.show_table()
    #database.insert_info('dbpython')
    database.close()