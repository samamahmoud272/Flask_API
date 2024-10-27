from .. import mongo  
from .models import Organization
from bson import ObjectId 
from flask import  jsonify

# create organization service 
def create_organization(name, description,current_user):
    
    # Get the identity of the current user
    if mongo.db.organizations.find_one({"name": name}):
        return {"message":"Organization with this name already exists."},400

    new_org = Organization(name, description,current_user)
    org_id = mongo.db.organizations.insert_one(new_org.__dict__).inserted_id
    
    return {"organization_id": str(org_id)}, 201

# Get organization service by organization_id
def get_organization(organization_id):
    try: 
        org = mongo.db.organizations.find_one({"_id": ObjectId(organization_id)})
        if org: 
            members =[]
            for member_id in org.get("members", []):
                 user = mongo.db.users.find_one({"_id": member_id})
                 members.append(
                     {
                    "name": user.get("name", ""),
                    "email": user.get("email", ""),
                    "access_level": "read_only" 
                     }
                 )     
            return {"organization_id": str(org["_id"]), "name": org.get("name", ""), 
                               "description": org.get("description", ""),"organization_members": members} , 200
        return {"message": "Organization not found"}, 404
        
    except:
            return {"message": "Failed to get organization check organization ID , Please try again."},500
 

# Update Organization Data service by organization_id
def update_organization(organization_id,name, description,current_user):
    
    update_fields = {}
    if name is not None:  
        update_fields["name"] = name
    if description is not None:  
        update_fields["description"] = description

    # If no fields are provided, return an error
    if not update_fields:
        return {"message": "At least one field (name or description) is required to update."}, 400
    
    #check if user is an organization member and have only read acsess 
    user = mongo.db.users.find_one({"email": current_user})
    if mongo.db.organizations.find_one({"_id": ObjectId(organization_id), "members": user["_id"]}):
        return {"message": "can't update this organization cause you have read only permission"}, 400
    

    try:
        org = mongo.db.organizations.find_one({"_id": ObjectId(organization_id)})
        if org:     
            # Update the organization in the database
            update_result = mongo.db.organizations.update_one(
                {"_id": ObjectId(organization_id)},
                {"$set": update_fields}
            )
        
            if update_result.modified_count > 0:
                # Fetch the updated organization to return its details
                updated_org = mongo.db.organizations.find_one({"_id": ObjectId(organization_id)})
                return {
                    "organization_id": str(updated_org['_id']),
                    "name": updated_org.get("name", ""),
                    "description": updated_org.get("description", "")}, 200
                
            return {"message": "Same Organization values exist, No changes made"}, 400  # No changes made to the record 
        
        return {"message": "Organization not found"}, 404
    except:
        return {"message": "An error occurred while updating the organization ."}, 500

# Delete Organization service by ID  
def delete_organization(organization_id,current_user):
    try: 
        org = mongo.db.organizations.find_one({"_id": ObjectId(organization_id)})
        if org:
            #check if user is an organization member and have only read acsess 
            user = mongo.db.users.find_one({"email": current_user})
            if mongo.db.organizations.find_one({"_id": ObjectId(organization_id), "members": user["_id"]}):
                return {"message": "can't Delete this organization cause you have read only permission"}, 400
            
        # Attempt to delete the organization from the database
            delete_result = mongo.db.organizations.delete_one({"_id": ObjectId(organization_id)})
            if delete_result.deleted_count > 0:
                 return {"message": "Organization deleted successfully."}, 200
             
        return {"message": "Organization not found."}, 404  
    
    except:
        return {"message": "An error occurred while Deleting the organization ."}, 500

         
# Invite User to organization's members service by user_email  
def invite_organization(organization_id,user_email):
    try: 
        org = mongo.db.organizations.find_one({"_id": ObjectId(organization_id)})
        user = mongo.db.users.find_one({"email": user_email})
        if org and user:
            if  mongo.db.organizations.find_one( {"_id": ObjectId(organization_id), "members": ObjectId(user["_id"])}):
                return {"message": " User already invited before successfully."}, 200
            if  mongo.db.organizations.find_one( {"created_by":user_email}):
                return {"message": "this User created the organization and can't be one of it's members"}, 400
            try:
                 # Add the user's ID to the organization's members array
                 mongo.db.organizations.update_one({"_id": ObjectId(organization_id)},{"$addToSet": {"members": ObjectId(user["_id"])}})
                 return {"message": " User invited successfully."}, 200
            except:
                 return {"message": " Failed to invite user , Please try again."}, 500        
        return {"message": "invited failed please check organization ID or user_email "}, 404
    except:
            return {"message": "Failed to get organization check organization ID , Please try again."},500
     
     
     
# Get All organization's information service  
def get_all_organizations():
    try: 
        orgs = mongo.db.organizations.find() 
        allorgs=[]
        for org in orgs:
            members=[]
            for member_id in org.get("members", []):  #get all members info 
                user = mongo.db.users.find_one({"_id": member_id})
                members.append({
                        "name": user.get("name", ""),
                        "email": user.get("email", ""),
                        "access_level": "read_only" 
                        })  
            #Append organization's info  to list of organization 
            allorgs.append({ 
                "organization_id": str(org["_id"]),  
                "name": org.get("name", ""),
                "description": org.get("description", ""),
                "organization_members": members
            })
        return allorgs,200
    except:
            return {"message": "Failed to get organizations , Please try again."},500