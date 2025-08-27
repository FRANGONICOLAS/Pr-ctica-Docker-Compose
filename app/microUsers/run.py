from users.views import app
from flask_cors import CORS

CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

