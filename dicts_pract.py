import requests

url_carts = "https://dummyjson.com/carts"

response = requests.get(url=url_carts)
data_from_net = response.json()
carts = data_from_net["carts"]

for items in carts:
    products = items["products"]
    for product in products:
        if product['discountPercentage'] >= 15:
            print(products["title"])
