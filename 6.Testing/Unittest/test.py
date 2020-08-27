import unittest # Se utiliza el modulo unitest para comprobar
from shopping import Item, ShoppingCart, NotExistsItemError

API = 17

class TestShopping(unittest.TestCase):  


    def setUp(self):
        self.pan = Item('Pan',20)
        self.jugo = Item('Jugo',30)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)
    
    #def tearDown(self):
        #print('Metodo teardown despues de la prueba')
    
    def test_suma_dos_positivos(self):
        assert 5 + 5 == 10

    def test_nombre_producto_igual_pan(self):
        #item = Item('Manzana',20)
        #self.assertEqual(item.name,'Manzana')
        self.assertEqual(self.pan.name, 'Pan')      # == assertEqual evalua un valor

    def test_nombre_producto_diferente_jugo(self):
        #item = Item('Pan Tostado',30)
        #self.assertNotEqual(item.name,'Manzana')
        self.assertNotEqual(self.jugo.name,'Pan')

    def test_contiene_pruductos(self):
        self.assertTrue(self.shopping_cart.contain_items())

    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contain_items())       
        
    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item,self.pan)       #is assertIs evalua un objeto
        self.assertIsNot(item,self.jugo)
    
    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)

    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total,0)
        self.assertLess(total,self.pan.price +1)
        self.assertEqual(total,self.pan.price)

    def test_codigo_pan(self):
        self.assertRegex(self.pan.code(),self.pan.name)

    def test_fail(self):
        if 2 > 3:
            self.fail('2 no es mayor a 3')

    #@unittest.skip('Se colocan los motivos')  #Se pone un decorardor para saltarse la prueba se utiliza python test.py -v para ver todas las pruebas
    #@unittest.skipIf(API < 18, 'La versión es obsoleta')
    #@unittest.skipUnless(3 > 5, '3 no es mayor a 5')
    def test_prueba_skip(self):
        pass

    #Libreria coverage, instalarla
    # Se utiliza la libreria coverage para ver el numero de test cubiertos, coverage report test.py
    # Se pone coverage run test.py, para correr todas las pruebas
    # Se vuelve a correr el reporte coverage report test.py, para ver que hace codigo no se usa 
    #coverage report -m test.py, da mas detalle se ve la linea de codigo que no se ha utilizado
    #Se elimina el codigo no necesario o se crea una prueba donde se utilice 
    #Para ver el reporte en html primero se corre coverage run test.py, y despues coverage html test.py
    # despues se pone python -m http.server
if __name__ == '__main__':
    unittest.main()
