import requests
import threading

key = 'e4cfac4208c75ddb73b30002dd322f4786684c2b'

def get_name():
    global key

    response = requests.get(f'https://calendarific.com/api/v2/holidays?&api_key={key}&country=MX&year=2020')
        
    if response.status_code == 200:  # Si esta bien sigue a payload
        
        payload = response.json()
        results = payload.get('response').get('holidays')  #{"meta":{"code":200},"response":{"holidays":[{"name":"New Year's Day",
        #results = payload['response']['holidays']
        if results:
            for result in results:
                result = result['name']
                print(result)   
        

if __name__ == '__main__':
    get_name()