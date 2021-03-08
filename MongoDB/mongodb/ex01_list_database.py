from pymongo import MongoClient

db_client = MongoClient("mongodb://localhost:27017/")

print(db_client.list_database_names())
