import requests

url = 'https://script.google.com/macros/s/AKfycbx5Cev1ZU1YMV5YUXx6oRhA4STiJk7Ie1EK_NAnpu7Mc2dC7ij9zCnYEygj8pG2BA8H/exec'

response = requests.get(url=url)
data_from_net = response.json()
print(data_from_net)
people = data_from_net["people"]

profit = 0
income_difference = 0
quantity_large_family = 0
quantity_poor_family = 0
quantity_women = 0
quantity_reach_women = 0

for data in people:
    income_difference = data["salary"] - data["credit_waste"]
    if income_difference < 0:
        quantity_poor_family += 1
    if data["large_family"]:
        quantity_large_family += 1
    if data["large_family"] and data["age"] > 35:
        profit = data["salary"] - data["credit_waste"]
    if data["sex"] == "female" and data["accomodation"]:
        quantity_reach_women += 1

