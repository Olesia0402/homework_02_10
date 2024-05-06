import json
from bson.objectid import ObjectId
from mongoengine import connect


conn  = connect(db='database', host="mongodb+srv://olesyashevchuk0402:JeJ6Bb00zAnOUTRL@cluster0.ki8cwf1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = conn.database
quotes_file = 'D:\Projects\my_repository\First_repo\homework_02_10\quotes\utils\quotes.json'

with open(quotes_file, 'r') as file:
    quotes = json.load(file)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quote.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })