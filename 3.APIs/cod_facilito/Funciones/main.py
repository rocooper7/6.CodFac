import requests
import json

def main(func,url,name_file):
    if func == 'get':   #Para obtener algun recurso
        response = requests.get(url,params = args_())
    elif func == 'post': #Para crear algun recurso
        response = requests.post(url,json=payload_(),headers=headers_())
                                    #json=payload() json post se encarga de serializarlos
                                    #data=json.dumbs(payload()) data nosotros tenemos que serializar 
    elif func == 'put': #Para actualizar algun recurso
        response = requests.put(url,json=payload_(),headers=headers_())
    else: #Para eliminarlo
        response = requests.delete(url,json=payload_(),headers=headers_())
    
    if response.status_code == 200:
        content = response.content
        print(response.url)

        #json_find(response)
        #headers_find(response)
        save_info(content,name_file)
    
def save_info(content,name_file):
    file = f'{name_file}'
    with open (file,'wb') as f:
        f.write(content)
        f.close()
  
def args_():     #get
   args = {'nombre':'Rodrigo','Curso':'Python', 'Nivel':'Intermedio'}
   return args

def payload_():  #post
    payload = {'nombre':'RODRIGO','Curso':'Python', 'Nivel':'Intermedio'}
    return payload

def headers_():   #post
    headers = {'Content_type':'app/json','Access_Token':'12345'}
    return headers

def json_find(response):   #get
    response_json = response.json()   #1forma
    origin = response_json['origin']
    print(origin)

    #response_json = json.loads(response.text)
    #origin = response_json['origin']
    #print(origin)

def headers_find(response): #post
    response_headers = response.headers
    server = response_headers['Server']
    print(server)

def chunks(url):  #Para una imagen
    response = requests.get(url,stream=True) #Se realiza la petición sin descargar el contenido
    with open('image.jpg','wb') as file:
        for chunk in response.iter_content(): #Descarga el contenido poco a poco
            file.write(chunk)
    response.close()

if __name__ == '__main__':
    main('get','https://www.google.com.mx/','google.html')
    #main('get','https://httpbin.org/get','binget.html')
    #main('post','https://httpbin.org/post','binpost.html')
    #main('put','https://httpbin.org/put','binput.html')
    #main('delete','https://httpbin.org/delete','bindelete.html')
    #chunks('https://studiosol-a.akamaihd.net/uploadfile/letras/fotos/3/1/b/9/31b910d182abe78f37609e199542ac1a.jpg')
        
