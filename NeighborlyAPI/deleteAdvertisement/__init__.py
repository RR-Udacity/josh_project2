import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get("id")

    if id:
        try:
            url = "mongodb://project2cosmodb:ldsE8YCzgTi8GFfR84wCimXVrZCLbrLbUXfj2uwVQKRB2kgyaLC7ZArYoKl1nhSYURsamm90fOZlhRqk9BnXoA==@project2cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmodb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client["project2db"]
            collection = database["advertisements"]

            query = {"_id": ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("{} was deleted.".format(id))

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse(
            "Please pass an id in the query string", status_code=400
        )
