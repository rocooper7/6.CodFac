import requests         #Se utiliza cuando hay un limite offset

def main(url,offset=0):
    args = {'offset':offset} if offset else {}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        content = response.content

        payload = response.json()
        results = payload.get('results',[])  #metodo de diccionario, si lo encuentras, me traes los resultados, sino nada
        if results:
            for result in results:
                result = result['name']
                print(result)

        next_ = input('Continuar listando [y/n]')
        next_= next_.lower()
        if next_ == 'y':
            main(url,offset=offset+20)

        

if __name__ == '__main__':
    main('https://pokeapi.co/api/v2/pokemon-form/')