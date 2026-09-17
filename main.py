import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 
                         "html.parser"
    )
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


