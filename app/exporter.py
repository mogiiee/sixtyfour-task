from dotenv import load_dotenv
import os

load_dotenv()

mongo_details = os.environ.get("CLUSTER")
collection = os.environ.get("collection")
database = os.environ.get("DB")
