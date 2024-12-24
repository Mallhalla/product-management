# run.py
from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

APP_HOST = os.environ.get()

if __name__ == '__main__':
    app.run(host=APP_HOST, port=5000)
