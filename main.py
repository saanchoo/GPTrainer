import os
from dotenv import load_dotenv

load_dotenv()

# Acceder a las variables
api_key = os.getenv("API_KEY")
# secret_key = os.getenv("SECRET_KEY")

print(f"API Key: {api_key}")