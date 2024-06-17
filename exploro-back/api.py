# flask --app api run -> Command to run FLask app
import datetime
import json
import random
from flask import Flask, jsonify, request
from connection import create_supabase_client

supabase = create_supabase_client()

app = Flask(__name__)
@app.route("/")
def hello():
    response =supabase.table("yodo").select("*").execute() #Selected all data from yodo table
    response = response.model_dump_json(indent=4)
    print(response)
    return response

@app.route("/posttest", methods=["GET"])
def postTest():
    if request.method != 'GET':
        return "Error"
    id = random.randint(1, 100)
    
    name = "Yodo " + str(id)
    data = {'name': name, 'id': id, "created_at": str(datetime.datetime.now())}
    response = supabase.table('yodo').insert(data).execute()

    return jsonify(response.data)   


@app.route("/post", methods=["POST"])
def post():

    # Get data from URL parameters
    id = request.args.get('id', default=random.randint(1, 100), type=int)
    
    name = request.args.get('name', default="Yodo " + str(id), type=str)

    response = supabase.table('yodo').select('id').eq('id', id).execute()
    if response.data:
        # ID already exists
        return jsonify({"error": "ID already exists"}), 400

    # Prepare data
    data = {'name': name, 'id': id, "created_at": str(datetime.datetime.now())}
    
    # Insert data into Supabase table
    response = supabase.table('yodo').insert(data).execute()
    print(jsonify(response.data))
    # Return the response data as JSON
    return jsonify(response.data)

@app.route("/put", methods=["PUT"])
def put():

    # Get data from URL parameters
    id = request.args.get('id', type=int)
    data = {"name": "PODA 00"}
    response = supabase.table('yodo').select('id').eq('id', id).execute()
    if response.data:
        # ID Doesn't exists
        response = supabase.table('yodo').update(data).eq('id', id).execute()
    else: 
        return jsonify({"error": "ID doesn't exists"}), 400
   
    # Return the response data as JSON
    return jsonify(response.data, "Updated")    

@app.route("/delete", methods=["DELETE"])
def delete():

    # Get data from URL parameters
    id = request.args.get('id', type=int)
    
    response = supabase.table('yodo').select('id').eq('id', id).execute()
    if not response.data:
        # ID already exists
        return jsonify({"error": "ID doesn't exists"}), 400
    else: 
        response = supabase.table('yodo').delete().eq('id', id).execute()
   

    # Return the response data as JSON
    return jsonify(response.data, "Deleted")


