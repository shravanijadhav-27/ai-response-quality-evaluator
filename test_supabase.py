
import tomllib
from supabase import create_client

with open(".streamlit/secrets.toml", "rb") as file:
    config = tomllib.load(file)

supabase = create_client(
    config["SUPABASE_URL"],
    config["SUPABASE_KEY"]
)

try:
    files = supabase.storage.from_("knowledge documents").list()

    print("SUCCESS: Bucket access is working!")
    print("Files found:", len(files))

    for file in files:
        print("-", file.get("name", "Unnamed file"))

except Exception as error:
    print("Bucket access failed:")
    print(type(error).__name__, str(error))
