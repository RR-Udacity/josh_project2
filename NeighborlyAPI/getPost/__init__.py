import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get("id")
    print("id: --------------->", id)

    if id:
        try:
            url = "mongodb://project2cosmodb:ldsE8YCzgTi8GFfR84wCimXVrZCLbrLbUXfj2uwVQKRB2kgyaLC7ZArYoKl1nhSYURsamm90fOZlhRqk9BnXoA==@project2cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmodb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client["project2db"]
            collection = database["posts"]

            query = {"_id": ObjectId(id)}
            # query = {"_id": id}
            # query = {"title": "Need a haircut!"}
            result = collection.find_one(query)
            print("----------result--------")
            result = dumps(result)
            print(result)

            return func.HttpResponse(
                result, mimetype="application/json", charset="utf-8"
            )
        except:
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse(
            "Please pass an id parameter in the query string.", status_code=400
        )
