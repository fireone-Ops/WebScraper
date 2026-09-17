import requests

URL = input("Digite a URL: ")

def validacao(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response)
        return response
    else:
        print(f". Status code: {response.status_code}")
        return None

response = validacao(URL)