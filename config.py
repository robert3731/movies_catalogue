import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
env_file = BASE_DIR / '.env'
load_dotenv(env_file)
API_TOKEN = os.environ.get('API_TOKEN')
SECRET_KEY = os.environ.get('SECRET_KEY')
