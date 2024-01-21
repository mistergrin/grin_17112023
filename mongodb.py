import pymongo
import config
import requests

url_quotes = "https://dummyjson.com/quotes?limit=100"


url = ("mongodb+srv://user21:{password}@clastertest.qr1sspj.mongodb.net/?retryWrites=true&w=majority".format
       (user=config.USER,
        password=config.PASSWORD,
        ))

client = pymongo.MongoClient(url)
db = client['quotes_data']
quotes = db['quotes']

response = requests.get(url=url_quotes)
data_from_net = response.json()
quotes_data = data_from_net["quotes"]


for data in quotes_data:
    quotes.insert_one(data)

query = {'author': "Albert Einstein"}
result = quotes.find(query)
print(result)

success_quotes = quotes.find({'quote': {'$regex': 'Success'}})
for text in success_quotes:
    print(text)

filter_data = {'author': 'Mark Twain'}
new_data = {'$set': {'favorite': True}}
processed = quotes.update_many(filter_data, new_data)

query_2 = {'author': "Vincent Van Gogh"}
deleted = quotes.delete_many(query_2)

quotes.drop()
