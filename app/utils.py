from flask_jwt_extended import create_access_token, create_refresh_token ,decode_token

def generate_token(identity):
    # Generate an access token.
    return create_access_token(identity=identity)

def generate_refresh_token(identity):
    # Generate a refresh token.
    return create_refresh_token(identity=identity)

def decode_jwt_token(token):
    # Decode refresh token
    decoded = decode_token(token)
    return decoded