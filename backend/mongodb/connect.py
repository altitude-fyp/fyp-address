import pymongo

client = pymongo.MongoClient("mongodb+srv://LZL:<password>@fypaddress.tefd1.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

print(db)