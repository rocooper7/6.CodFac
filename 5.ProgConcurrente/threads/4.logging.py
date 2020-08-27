import logging

# Debug (10), Info (20), Warning (30), Error (40), Critical (50)

#logging

logging.basicConfig(
    level=logging.DEBUG,#10
    format='%(filename)s Msj: %(message)s, Función:%(funcName)s, %(levelname)s, Linea de ejecución: %(lineno)s, thread: %(thread)s',
    datefmt='%H:%M:%S',
    #filename='messages.txt'  Para almacenar msjs
)

def mis_mensajes():
    logging.debug('Este es un mensaje de tipo Debug')
    logging.info('Este es un mensaje de tipo Info')
    logging.warning('Este es un mensaje de tipo Warning')
    logging.error('Este es un mensaje de tipo Error')
    logging.critical('Este es un mensaje de tipo Critical')

if __name__ == '__main__':
    mis_mensajes()
    