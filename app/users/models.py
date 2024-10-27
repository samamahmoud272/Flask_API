from .. import mongo  
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password  
        
    
    def create_index():
        # Create a unique index on the email field
        mongo.db.users.create_index("email", unique=True)    