from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("AZURE_ENDPOINT"))
print(os.getenv("AZURE_KEY"))