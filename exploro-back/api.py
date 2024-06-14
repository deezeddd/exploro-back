# flask --app api run -> Command to run FLask app
import json
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


