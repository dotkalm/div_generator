from flask import Flask
from flask_cors import CORS
from api.api import api
import os

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

CORS(api, origins=['http://localhost:3000', 'https://joelholmberg.com'], supports_credentials=True)
app.register_blueprint(api)

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'hi'

if 'ON_HEROKU' in os.environ:
    print('hitting ')
    models.initialize()

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)

