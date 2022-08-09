from flask import Flask, render_template, request, jsonify
from flask_pymongo import pymongo

app = Flask(__name__)

CONNECTION_STRING = "mongodb+srv://root:root@cluster0.dawzd2z.mongodb.net/?retryWrites=true&w=majority"


@app.route("/add_one", methods = ['POST'])
def add_one():
    if request.method == 'POST':
        coll = str(request.json['collection_name'])
        data = request.json['data']

        try:

            client = pymongo.MongoClient(CONNECTION_STRING)

            db = client.test
            mydb = client["FLASKCRUD"]
            mycollection = mydb[coll]
            mycollection.insert_one(data)

        except Exception as e:
            client.close()

        return str(mycollection)


@app.route("/get_all", methods=['POST'])
def get_all():
    if request.method == 'POST':
        col_data = str(request.json['collection_name'])
        #data = request.json['data']

        try:

            client = pymongo.MongoClient(CONNECTION_STRING)

            result = []
            mydb = client["FLASKCRUD"]
            col = mydb[col_data]
            res = col.find()
            for x in res:
                result.append(x)

        except Exception as e:
            client.close()

        return str(result)


@app.route("/get_one", methods=['POST'])
def get_one():
    if request.method == 'POST':
        col_data = str(request.json['collection_name'])
        data = request.json['data']

        try:

            client = pymongo.MongoClient(CONNECTION_STRING)

            result = []
            mydb = client["FLASKCRUD"]
            col = mydb[col_data]
            data1 = data
            res = col.find_one(data1)


        except Exception as e:
            client.close()
            print("Error "+str(e))

        return str(res)


if __name__ == '__main__':
    app.run()
