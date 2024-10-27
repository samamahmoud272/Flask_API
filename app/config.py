from dotenv import load_dotenv
import os
class Config:
    load_dotenv()  # Load environment variables from .env file
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time  (1 hour)
    JWT_REFRESH_TOKEN_EXPIRES = 604800  # Refresh token expiration time (1 week)