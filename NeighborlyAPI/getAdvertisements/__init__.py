import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://iandbp2:Jtjt2LUoLaukoMUTtjGdtjhFg1VH6DBDHpNhbQT7cgjdK12PALg2oEZ9ymGlKe0rFBAs7U1OflJpZ71bxfTasw==@iandbp2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@iandbp2@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client["neighborapp"]
        collection = database["advertisements"]

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb", status_code=400)
