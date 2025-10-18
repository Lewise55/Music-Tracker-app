from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Song
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity, jwt_required, JWTManager, create_access_token
import hashlib
api = Blueprint('api', __name__)

# allow Cors request to this api
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    
    response_body ={
        "message": "This message will apear if the backend is working"
    }

    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def handle_signup():
    body = request.json
    
@api.route('/login', methods=['POST', 'GET'])
def handle_login():

@api.route('/profile', methods=['POST', 'GET'])
def handle_profile():
