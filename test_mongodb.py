
import tomllib
from pathlib import Path
from pymongo import MongoClient

# Read MongoDB credentials
with open(".streamlit/secrets.toml", "rb") as file:
    secrets = tomllib.load(file)

try:
    client = MongoClient(
        secrets["MONGODB_URI"],
        serverSelectionTimeoutMS=10000
    )

    client.admin.command("ping")

    print("MongoDB Atlas connected successfully!")
    print("Database:", secrets["MONGODB_DATABASE"])

    client.close()

except Exception as error:
    print("Connection failed:", error)
