import requests
import json

url = 'https://dummyjson.com/quotes?limit=100'

response = requests.get(url=url)
data = response.json()

with open('data.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)

