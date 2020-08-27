import requests        #Para cortar una ejecución muy larga Ctrl + C
import time
import json


if __name__ == '__main__':
    response = requests.get('https://formulae.brew.sh/api/formula.json')
    packages_json = response.json()   #o se puede usar content en lugar de json()
    
    package_list = []
    t1 = time.perf_counter()
    
    for package in packages_json:         #En vez de esto se podria hacer una funcion search como en el crud y usar found
        if package['name'] == 'carina':
            continue
        elif package['name'] == 'zrepl':
            continue
                    
        package_name = package['name']
        package_desc = package['desc']

        response = requests.get(f'https://formulae.brew.sh/api/formula/{package_name}.json')
        package_json = response.json()    
        package_str = json.dumps(package_json, indent = 2)  #Para darle formato al json
        

        day_30 = package_json['analytics']['install_on_request']['30d'][package_name]
        day_90 = package_json['analytics']['install_on_request']['90d'][package_name] 
        day_365 = package_json['analytics']['install_on_request']['365d'][package_name]    
        
        data = {
            'name': package_name,
            'desc': package_desc,
            'analytics':{
                '30d':day_30,
                '90d':day_90,
                '365d':day_365
                }
            }
        
        package_list.append(data)

        #time.sleep(response.elapsed.total_seconds())
        print(f'Got {package_name}') #in {response.elapsed.total_seconds()} seconds')

        #break

    t2 = time.perf_counter()
    print(f'Finished in {t2-t1} seconds')

    with open('package_info.json','w') as f:
        json.dump(package_list,f,indent=2)

        
         


        
        
