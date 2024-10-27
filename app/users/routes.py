from flask import Blueprint, request, jsonify
from .services import signup,signin

api = Blueprint('user_routes', __name__)

# Route to registercnew user 
@api.route('/signup', methods=['POST'])
def signup_route():
    data = request.json
    return signup(data['name'], data['email'], data['password'])

# Route to sign in  
@api.route('/signin', methods=['POST'])
def signin_route():
    data = request.json
    return signin(data['email'], data['password'])

# Route to refresh token 
@api.route('/refresh-token', methods=['POST'])
def refresh_token_route():
    from .services import refresh_token
    data = request.json
    return refresh_token(data['refresh_token'])