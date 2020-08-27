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
    user = peewee.ForeignKeyField(User,related_name='stores')  #Relación 1 a muchos
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
    name = peewee.CharField(max_length=50)  #Relación 1 a muchos
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store,related_name='products')
    price = peewee.DecimalField(max_digits=5,decimal_places=2)
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        table_name = 'products'

    def __str__(self):
        return f'{self.name} - ${self.price}'

class Category(peewee.Model):
    name = peewee.CharField(max_length=50)
    description = peewee.TextField()
    active = peewee.BooleanField(default=True)
    create_date = peewee.DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db
        table_name = 'categories'

    def __str__(self):
        return self.name

class ProductCategory(peewee.Model):
    product = peewee.ForeignKeyField(Product,related_name='categories')
    category = peewee.ForeignKeyField(Category,related_name='products')

    class Meta:
        database = db
        table_name = 'product_categories'
    
    def __str__(self):
        return f'{self.product} - {self.category}'