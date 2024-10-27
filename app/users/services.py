from .. import mongo  
from .models import User
from ..utils import generate_token, generate_refresh_token,decode_jwt_token  
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

# Register new user service 
def signup(name, email, password):
    hashed_password =generate_password_hash(password)
    user =mongo.db.users.find_one({"email": email})
    if user:   
        return {"message": "User already exist , Please try again."},400
    try:
        new_user = User(name, email, hashed_password)
        mongo.db.users.insert_one(new_user.__dict__)
        return {"message": "User registered successfully"}, 201
    except:
        return {"message": "Failed to register new user , Please try again."},500


# sign in user service 
def signin(email, password):
    user = mongo.db.users.find_one({"email": email})  
    if user and check_password_hash(user['password'], password):  
        access_token = generate_token(identity=user['email']) 
        refresh_token = generate_refresh_token(identity=user['email'])
        return {
            "message": "Login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 200
    return {"message": "Invalid credentials"}, 401

def refresh_token(refresh_token):
    # Validate the refresh token input
    if not refresh_token:
        return {"message": "Refresh token is required."}, 400    

    # Decode the refresh token to get the identity
    decoded_token = decode_jwt_token(refresh_token)
    
    # Check if the token is a refresh token
    if decoded_token.get('type') != 'refresh':
        return {"message": "Invalid token type."}, 401 

    # Check for expiration
    exp = decoded_token.get('exp')
    if exp and datetime.utcfromtimestamp(exp) < datetime.utcnow():
        return {"message": "Token expired."}, 401 

    current_user = decoded_token['sub'] 

    access_token = generate_token(identity=current_user)  
    new_refresh_token = generate_refresh_token(identity=current_user)  

    return {
        "message": "Tokens refreshed successfully",
        "access_token": access_token,
        "refresh_token": new_refresh_token
    }, 200