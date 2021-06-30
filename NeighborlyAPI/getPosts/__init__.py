import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Python getPosts trigger function processed a request.")

    try:
        url = "mongodb://project2cosmodb:ldsE8YCzgTi8GFfR84wCimXVrZCLbrLbUXfj2uwVQKRB2kgyaLC7ZArYoKl1nhSYURsamm90fOZlhRqk9BnXoA==@project2cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmodb@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client["project2db"]
        collection = database["posts"]

        result = collection.find({})
        print("----------result--------")

        result = dumps(result)
        print(result)

        return func.HttpResponse(
            result, mimetype="application/json", charset="utf-8", status_code=200
        )
    except:
        return func.HttpResponse("Bad request.", status_code=400)
