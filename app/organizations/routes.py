from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .services import create_organization ,get_organization ,update_organization , delete_organization ,invite_organization,get_all_organizations # Import your service function

api = Blueprint('organization_routes', __name__)

# Route to create organization 
@api.route('/organization', methods=['POST'])
@jwt_required()  # Ensure the user is authenticated
def create_organization_route():
    data = request.json
    
    if not data or 'name' not in data or 'description' not in data:
        return {"message": "Name and description are required."}, 400

    current_user = get_jwt_identity()
    # Call the service function to create the organization
    return create_organization(data['name'], data['description'],current_user)
    
# Route to Get organization by organization_id
@api.route('/organization/<string:organization_id>', methods=['GET'])
@jwt_required()  # Ensure the user is authenticated
def get_organization_route(organization_id):

    return  get_organization(organization_id)

# Route to update organization by organization_id
@api.route('/organization/<string:organization_id>', methods=['PUT'])
@jwt_required()  # Ensure the user is authenticated
def update_organization_route(organization_id):
   data = request.json
   current_user = get_jwt_identity()
   return  update_organization(organization_id,data['name'], data['description'],current_user)

 # Route to delete organization
@api.route('/organization/<string:organization_id>', methods=['DELETE']) 
@jwt_required()
def delete_organization_route(organization_id):
    current_user = get_jwt_identity()
    return delete_organization(organization_id,current_user)
        
# Route to invite user to  organization's members
@api.route('/organization/<string:organization_id>/invite', methods=['POST'])
@jwt_required()  # Ensure the user is authenticated
def invite_organization_route(organization_id):
    data = request.json
    return  invite_organization(organization_id,data['user_email'])        

# Route to get all organizations
@api.route('/organization', methods=['Get'])
@jwt_required()  # Ensure the user is authenticated
def get_all_organization_route():
    # Call the service function to get all organizations
    return get_all_organizations()