import json
from pymongo import MongoClient 
  
  
# Making Connection
myclient = MongoClient("mongodb://project2cosmodb:ldsE8YCzgTi8GFfR84wCimXVrZCLbrLbUXfj2uwVQKRB2kgyaLC7ZArYoKl1nhSYURsamm90fOZlhRqk9BnXoA==@project2cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmodb@") 
   
# database 
db = myclient["project2db"]
   
# Created or Switched to collection 
# names: GeeksForGeeks
Collection = db["advertisements"]
  
# Loading or Opening the json file
with open('sampleAds.json') as file:
    file_data = json.load(file)
      
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)  
else:
    Collection.insert_one(file_data)