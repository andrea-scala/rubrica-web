from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def index():
    return 'Rubrica Web - ok'

if __name__ == '__main__':
    app.run(debug=True)
