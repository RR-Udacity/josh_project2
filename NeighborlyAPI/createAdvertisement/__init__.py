import azure.functions as func
import pymongo
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    print("request: {}".format(dumps(request)))

    if request:
        try:
            url = "mongodb://iandbp2:Jtjt2LUoLaukoMUTtjGdtjhFg1VH6DBDHpNhbQT7cgjdK12PALg2oEZ9ymGlKe0rFBAs7U1OflJpZ71bxfTasw==@iandbp2.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@iandbp2@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client["neighborapp"]
            collection = database["advertisements"]
            print("request: {}".format(dumps(request)))

            # rec_id1 = collection.insert_one(eval(request))
            rec_id1 = collection.insert_one(request)
            print("Inserted Id: {}".format(rec_id1.inserted_id))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse("Could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass name in the body", status_code=400)
