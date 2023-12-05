import requests

url_carts = "https://dummyjson.com/carts"

response = requests.get(url=url_carts)
data_from_net = response.json()
carts = data_from_net["carts"]

for items in carts:
    product = items["products"]
    for products in product:
        if products['discountPercentage'] >= 15:
            print(products["title"])
