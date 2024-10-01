"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Measure
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


    

@api.route("/send_all", methods=["GET"])
def all_measures():

    dictionary= {"message" : "hello world"}

    measure=Measure.query.all()
    all_measures = list(map(lambda x: x.serialize(), measure))

    return jsonify(all_measures), 200

@api.route('/newmeasure', methods=['POST'])
def new_measure():

    request_body=request.get_json()
    
    new_measure = Measure(position=request_body["position"], date=request_body["date"], temperature=request_body["temperature"], hour=request_body["hour"])

    db.session.add(new_measure)
    db.session.commit()

    return jsonify("Measure added correctly"), 200
