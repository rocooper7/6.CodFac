from pymongo import MongoClient
import re


client = MongoClient()
db = client['minicurso_python']

def insert_many():
    user1 = {'username': 'codigofacilito1', 'password': 'password123', 'age' : 23}
    user2 = {'username': 'codigofacilito2', 'password': 'password123', 'age' : 24}
    user3 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 25}
    user4 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 26}

    db.users.insert_many( [user1, user2, user3, user4] )

def insert_one():
    user = {'username': 'codigofacilito4', 'password': 'password123', 'age' : 27}
    db.users.insert_one(user)
    #result = db.users.insert_one(user)
    #print(result.inserted_id)

def find_user():
    users = db.users.find()  #Buscar a todos los documentos
    #users = db.users.find({'age':23})  #Vusca un solo documento
    #user= db.users.find({'username':'codigofacilito1'}).count()  #Cuenta lo que se tiene que buscar, sin el ciclo for
    #print(user)
    #users= db.users.find({'username':'codigofacilito1'}).limit(1)  #Trae el limite que se requiere

    #user = db.users.find_one()
    #user = db.users.find_one({'username' : 'codigofacilito1'})
    #print(user)
    #users = db.users.find({"$or":[ {'username':'codigofacilito1'}, {'age':23} ]})
    #users = db.users.find({"$and":[ {'username':'codigofacilito1'}, {'age':23} ]})  
    
    for user in users:
        print(user)

def update():
    db.users.update_one({'username': 'codigofacilito1'}, {'$set' : { 'age' : 31}  })
    db.users.update_many({'password': 'password123'}, {'$inc': {'age': 1}})  #Incrementa la edad 1 año a todos

def delete():
    db.users.delete_one({'username': 'codigofacilito1'})
    #db.users.delete_many({'password': 'password123'})

def consultas():
    #regex = re.compile('codigo')  # LIKE %codigo%
    #regex = re.compile('^codigo')  # LIKE %codigo
    #regex = re.compile('codigo$')     # LIKE codigo%
     
    users = db.users.find_one({'username' : regex })
    for user in users:
        print(user)

if __name__ == '__main__':
    #insert_many()
    #insert_one()
    #find_user()
    #update()
    #delete()
    consultas()