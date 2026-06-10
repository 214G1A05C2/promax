from flask import Flask
from flask_cors import CORS

from config import Config

from models.call_metrics_model import db

from api.call_metrics_api import call_metrics_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

# Initialize Database
db.init_app(app)

# Register API Blueprint
app.register_blueprint(call_metrics_bp)

# Home Route
@app.route("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }

# Run Server
if __name__ == "__main__":
    app.run(debug=True, port=8000)