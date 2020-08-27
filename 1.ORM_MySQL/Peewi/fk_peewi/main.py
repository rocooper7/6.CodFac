import peewee
from models import User,Store,Product,Category,ProductCategory

def create_table(class_name):
    if class_name.table_exists():
        class_name.drop_table()

    class_name.create_table()

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
    elif table_name == 'categories':
        category = Category.create(name = 'Liquidos',description ='liquidos')
        category = Category.create(name = 'Embutidos',description ='embutidos')
        category = Category.create(name = 'Snacks',description ='snacks')
        category = Category.create(name = 'Aderezos',description ='aderezos')
        category = Category.create(name = 'Carnes',description ='carnes')
        category.save()
    elif table_name == 'product_categories':
        ProductCategory.create(category_id=1,product_id =2)
        ProductCategory.create(category_id=1,product_id =4)
        ProductCategory.create(category_id=2,product_id =3)
        ProductCategory.create(category_id=3,product_id =5)
        ProductCategory.create(category_id=4,product_id =6)
        ProductCategory.create(category_id=5,product_id =3)

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

def delete_instance():
    jamon = Product.get(Product.name == 'Jamon')
    jamon.delete_instance(recursive= True)

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
    #for store in user.stores:
        #print(store)

    query = (Product.select()
    .join(Store)
    .join(User)
    .where(User.id == f'{id}')
    .order_by(Product.price.desc()))

    for product in query:
        print(product)

    print('*'*10)

def relacion2():     #Relacion Muchos a Muchos
    categories = Category.select()
    for category in categories:
        print(f'>> {category}')
        for product in category.products:
                print(product)
    
    print('*'*50)
    jamon = Product.get(Product.name == 'Jamon')
    for category in jamon.categories:
        print(category)

    print('*'*50)
    liquido = Category.get(Category.name == 'Liquidos')
    for product in liquido.products:
        print(product)

def create_schema():
    create_table(User)
    create_table(Store)
    create_table(Product)
    create_table(Category)
    create_table(ProductCategory)
    insert_data('users')
    insert_data('stores')
    insert_data('products')
    insert_data('categories')
    insert_data('product_categories')


if __name__ == '__main__':
    
    create_schema()
    #get_user(1)
    #get_all_users(1,'Xbox')
    #update(1,'Aldo')
    #delete(2)
    #count()
    #user_exists(1)
    #relaciones(1)
    #relacion2()

