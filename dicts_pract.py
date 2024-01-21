import requests

url_carts = "https://dummyjson.com/carts"

response = requests.get(url=url_carts)
data_from_net = response.json()
carts = data_from_net["carts"]

for users_purchase in carts:
    products = users_purchase["products"]
    if users_purchase["userId"] == 56:
        for product in products:
            if product['discountPercentage'] >= 15:
                print(product["title"])
