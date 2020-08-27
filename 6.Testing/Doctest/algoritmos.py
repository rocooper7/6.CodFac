""" 
>>> recursivo = Recursivo()
>>> recursivo.factorial(5)
120
"""

def fibonacci(number):
    if number == 0: return 0
    elif number == 1: return 1
    else: return fibonacci(number-1) + fibonacci(number-2)

def palindromo(sentence):
    """Retorna True si el parametro es un palindromo
    en caso contrario regresa False

    sentence -- String o entero

    >>> palindromo('anita lava la tina')
    True
    >>> palindromo(12321)
    True
    >>> palindromo('CodigoFacilito')
    False
    """
    sentence = str(sentence).lower().replace(" ","")
    return sentence == sentence[::-1]

class Recursivo():
    def factorial(self,number):
        if number == 0: return 1
        else: return number * self.factorial(number - 1)
        print (number)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile('test.txt')   #Se pone python algoritmos.py -v