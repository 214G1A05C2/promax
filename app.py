import os

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

with app.app_context():
    db.create_all()

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
    port = int(os.environ.get("PORT", 8000))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"

    app.run(host="0.0.0.0", port=port, debug=debug)
