import dotenv
import os

try:
    dotenv.load_dotenv()
    wolframalpha_id = os.getenv("wolframalpha_id")
except:
    wolframalpha_id = os.environ.get("wolframalpha_id")
