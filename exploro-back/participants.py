# flask --app api run -> Command to run FLask app
import datetime
import json
import random
from flask import Flask, jsonify, request
from connection import create_supabase_client

supabase = create_supabase_client()

app = Flask(__name__)
@app.route("/participantAll")
def participantAll():
    response =supabase.table("Participant").select("*").execute() #Selected all data from yodo table
    response = response.model_dump_json(indent=4)
    print(response)
    return response

@app.route("/userStudies", methods=["GET"])
def postTest():
    response =supabase.table("UserStudies").select("*").execute() #Selected all data from yodo table
    response = response.model_dump_json(indent=4)
    print(response)
    return response


