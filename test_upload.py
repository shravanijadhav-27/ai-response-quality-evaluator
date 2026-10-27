
import tomllib
from pathlib import Path
from supabase import create_client

with open(".streamlit/secrets.toml", "rb") as file:
    config = tomllib.load(file)

supabase = create_client(
    config["SUPABASE_URL"],
    config["SUPABASE_KEY"]
)

test_file = Path("upload_test.txt")
test_file.write_text(
    "Test document for AI Response Quality Evaluator."
)

try:
    with test_file.open("rb") as file:
        supabase.storage.from_("knowledge-documents").upload(
            path="upload_test.txt",
            file=file,
            file_options={"upsert": "true"}
        )

    print("SUCCESS: Test document uploaded!")

except Exception as error:
    print("Upload failed:")
    print(type(error).__name__, str(error))
