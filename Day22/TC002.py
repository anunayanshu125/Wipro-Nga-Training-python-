
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["Wipro"]

collection = db["Employee"]

#inserting the record

result = collection.insert_one({"name": "Anunay", "age": 25, "salary": "50000"})

#finding the inserted or existing record

result1 = collection.find({"name": "Anunay"})

documents = list(result1)

print(documents)
