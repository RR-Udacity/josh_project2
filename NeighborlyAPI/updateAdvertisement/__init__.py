import azure.functions as func
import pymongo
from bson.objectid import ObjectId
from icecream import ic
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get("id")
    request = req.get_json()

    if request:
        try:
            url = "mongodb://project2cosmodb:ldsE8YCzgTi8GFfR84wCimXVrZCLbrLbUXfj2uwVQKRB2kgyaLC7ZArYoKl1nhSYURsamm90fOZlhRqk9BnXoA==@project2cosmodb.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2cosmodb@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client["project2db"]
            collection = database["advertisements"]
            ic(request)

            filter_query = {"_id": ObjectId(id)}
            update_query = {"$set":request}
            ic(filter_query)
            ic(update_query)
            rec_id1 = collection.update_one(filter_query, update_query)
            # rec_id1 = collection.update_one({"_id": ObjectId(id)},{"$set": {"title": "My Updated Title"}})
            ic(rec_id1)
            return func.HttpResponse("{} Updated".format(id), status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse("Could not connect to mongodb", status_code=500)
    else:
        return func.HttpResponse("Please pass name in the body", status_code=400)
