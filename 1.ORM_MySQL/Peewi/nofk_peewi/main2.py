import peewee
import datetime

db = peewee.MySQLDatabase(
            database = 'dbpython',
            host = 'localhost', 
            port = 3306, 
            user = 'root',
            password = 'Cooperboy0071985')

class User(peewee.Model):
    username = peewee.CharField(unique=True,max_length=50,index=True)
    age = peewee.IntegerField()
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(unique=True,max_length=50,null=True)
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        table_name = 'users'
    
    def __str__(self):
        return self.username

class Store(peewee.Model):
    #user = peewee.ForeignKeyField(User,primary_key=True) #Relación 1 a 1 
    #user = peewee.ForeignKeyField(User,related_name='stores')  #Relación 1 a muchos
    user_id = peewee.IntegerField()
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        table_name = 'stores'

    def __str__(self):
        return self.name

class Product(peewee.Model):
    store_id = peewee.IntegerField()
    name = peewee.CharField(max_length=50)  #Relación 1 a muchos
    description = peewee.TextField()
    #store = peewee.ForeignKeyField(Store,related_name='products')
    price = peewee.DecimalField(max_digits=5,decimal_places=2)
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        table_name = 'products'

    def __str__(self):
        return f'{self.name} - ${self.price}'

def create_table():
    if User.table_exists():
        User.drop_table()

    User.create_table()
    
    if Store.table_exists():
        Store.drop_table()

    Store.create_table()

    if Product.table_exists():
        Product.drop_table()

    Product.create_table()

def insert_data(table_name):
    if table_name == 'users':
        user = User.create(username='Aldo',age=30,password='Xbox',email='cooperboy008@hotmail.com')
        user = User.create(username='Rodrigo',age=35,password='Cooper',email='rgcooper85@gmail.com')
        user = User.create(username='Nora',age=60,password='sldld',email='nora@gmail.com')
        user = User.create(username='Salvador',age=68,password='dhdhf',email='salv@gmail.com')
        user = User.create(username='Sara',age=23,password='sllswso',email='sara@gmail.com')
        user.save()
    elif table_name == 'stores':
        store = Store.create(user_id = 1,name='La esquina',address='Fuentes del Molino #10')
        store = Store.create(user_id = 1,name='Don Simon',address='Fuentes del Molino #12')
        store = Store.create(user_id = 1,name='Carmelita',address='Fuentes del Molino #13')
        store = Store.create(user_id = 4,name='Wallis',address='Fuentes del Molino #14')
        store = Store.create(user_id = 5,name='Don perse',address='Fuentes del Molino #16')
        store.save()
    elif table_name == 'products':
        product = Product.create(store_id = 1,name='Pan',description='Pan Integral',price=5.5,stock=10)
        product = Product.create(store_id = 1,name='Leche',description='Baja en grasas',price=15.5,stock=24)
        product = Product.create(store_id = 1,name='Jamon',description='Pavo',price=45.5,stock=10)
        product = Product.create(store_id = 2,name='Soda',description='Dieta',price=10.5,stock=10)
        product = Product.create(store_id = 2,name='Fritura',description='Churros',price=9.5,stock=10)
        product = Product.create(store_id = 2,name='Salsa',description='Habanero',price=11.5,stock=10)
        product.save()

def get_user(id):
    user = User.get(User.id == f'{id}')
    print(user)
    #users = User.select().where(User.id > f'{id}').limit(4).order_by(User.id.asc())
    #for user in users:
        #print(user)
    #last_user = User.select().order_by(User.id.desc()).limit(1).get()
    #print(last_user)    

def get_all_users(id,password):
    users = User.select(User.username,User.age,User.password,User.email)#.where( (User.id == f'{id}') and (User.password == f'{password}') )
    for user in users:
        print(f'Username:{user.username}| Age:{user.age}| Password:{user.password}| Eamil:{user.email}')
    
def update(id,username):
    user = User.update(username=f'{username}',active=True).where(User.id == f'{id}')
    user.execute()

def delete(id):
    user = User.delete().where(User.id == f'{id}')
    user.execute()

def count():
    count = User.select().count()
    print(count)

def user_exists(id):
    try:
        user = User.get(User.id == f'{id}')
        print(user)    
    except Exception as e:
        print('El id_usuario no existe')
    
    #user = User.select().where(User.id == f'{id}').first()
    #if user:
        #print('El usuario existe')
    #else:
        #print('El usuario no existe')

def relaciones(id):
    #tienda = Store.get(Store.user_id == f'{id}')
    #print(tienda.user)#.password)
    
    #user = User.get(User.id == f'{id}')   # query para dos tablas
    #print(user)
    #for store in user.store:
        #print(store)
    
    query = (Product.select()
    .join(Store, on=(Product.store_id == Store.id))
    .join(User, on=(Store.user_id == User.id))
    .where(User.id == f'{id}')
    .order_by(Product.price.desc()))

    for product in query:
        print(product)

def create_schema():
    create_table()
    insert_data('users')
    insert_data('stores')
    insert_data('products')


if __name__ == '__main__':
    
    #create_schema()
    #get_user(1)
    #get_all_users(1,'Xbox')
    #update(1,'Aldo')
    #delete(2)
    #count()
    #user_exists(1)
    relaciones(1)




