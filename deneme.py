import requests

hak = int(input('kaç hak istersiniz: '))
sayac=0

while hak > 0:
    template_id = input('TEMPLATE ID giriniz: ')

# url ve postman adresinizi giriniz.
    url = 'URL'

    myobj = {
    "jsonrpc": "2.0",
    "params": {
        "template_id": template_id


        }
    }



    x = requests.post(url, json = myobj)
    response = x.json()['result']['response']['template'][0]
    if response['state'] == 'live':
        print('dev ya da stage de çalışır')
    else:
        print(response)
    hak -= 1
    if hak == 0:
        print('hakkınız bitmiştir')
    
        
        
    