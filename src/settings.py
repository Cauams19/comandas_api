from dotenv import load_dotenv, find_dotenv
import os

# Tracks the .env file
dotenv_file = find_dotenv()

# Loads the .env file
load_dotenv(dotenv_file)

# Defining API settings
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
RELOAD = os.getenv("RELOAD")