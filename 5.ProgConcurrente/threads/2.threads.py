import requests
import threading

def get_name():
    response = requests.get('https://api.datos.gob.mx/v1/condiciones-atmosfericas')
        
    if response.status_code == 200:  # Si esta bien sigue a payload
        
        payload = response.json()
        results = payload.get('results')  
        name = results[0].get('name')
        print(name)

if __name__ == '__main__':
    
    for _ in range(0,20):
        thread = threading.Thread(target=get_name)    #Se aplica el thread para hacer 
        thread.start()