import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging


def main(req: func.HttpRequest) -> func.HttpResponse:

    # example call http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get("id")
    print("--------------->", id)

    if id:
        try:
            url = "mongodb://iandbp2:Jtjt2LUoLaukoMUTtjGdtjhFg1VH6DBDHpNhbQT7cgjdK12PALg2oEZ9ymGlKe0rFBAs7U1OflJpZ71bxfTasw==@iandbp2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@iandbp2@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client["neighborapp"]
            collection = database["advertisements"]

            # query = {"_id": ObjectId(id)}
            # query = {"_id": id}
            # result = collection.find_one(query)
            result = collection.find_one({"_id": ObjectId(id)})
            print("----------result--------")
            print("id: {}".format(id))

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
