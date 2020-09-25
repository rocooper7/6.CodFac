import requests
#https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/ #1
client_id = '807fb01066ec696dba0d'    #1 Se crea una sesion en oath y se consigue client_id y client_secret
client_secret = '2499f0004a310212f255291302a90450901ef72c'
#https://github.com/login/oauth/authorize?client_id=807fb01066ec696dba0d&scope=repo  #1 Se copia de la pagina oath, 
# se le agrega la info, que se consiguio y se accesa a la pagina y se consigue el code
code='22eebf56aa8c3d5a630f'  #code caduca despues de cierto tiempo, para sacarlo nuevamente
access_token = '5e61c97fa016df1c7d0884fea22d1bfa8bd45f7b'

def paso_1(url): #Obtener token
    payload = {'client_id':client_id,'client_secret':client_secret,'code':code}
    headers = {'Accept': 'application/json'}
    
    response = requests.post(url,json=payload,headers=headers)
    
    if response.status_code == 200:
        response_json = response.json()
        access_token = response_json['access_token']
        print(access_token)  

def lista_repos(url):  #Iterar sobre los repos
    headers = {'Authorization': f'token {access_token}'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        for project in response_json:
            name = project['name']
            print(name)
    else:
        print(response.content)  

def create(url):  #crear un repositorio nuevo
    payload = {'name':'git_api_cf_comunidad'}  #Cambiar el nombre para que funcione
    headers = {'Accept': 'application/json','Authorization': f'token {access_token}'}
    response = requests.post(url,headers=headers,json= payload,)
    if response.status_code == 200:
       response_json = response.json()
       for project in response_json:
           name = project['name']
           print(name)
    else:
        print(response.content)  
        
def cookies(url):
    cookies = {'my_cookies':'True'}
    response = requests.get(url,cookies=cookies)
    
    if response.status_code == 200:
        cookies = response.cookies
        print(cookies)
        print('El contenido es:')
        print(response.content)

def sesiones(url):
    session = requests.session()
    session.auth = ('rgcooper85@gmail.com','RobertoCooper0071985')

    response = session.get(url)
    print(response.content)
    
    if response.ok:
        response = session.get('https://github.com/rocooper7/RodrigoCoding')
        print(response.cookies)
        

if __name__ == '__main__':
    #paso_1('https://github.com/login/oauth/access_token') #2 Se copia la direccion de la pagina oath para sacar el token
    #lista_repos('https://api.github.com/user/repos') #3De esta pagina se saca el contenido #https://developer.github.com/v3/repos/#get
    #create('https://api.github.com/user/repos')
    #cookies('https://httpbin.org/cookies')
    sesiones('https://api.github.com/user')