from flask import Flask
from flask_cors import CORS

from app.database import init_db
from app.routes.home_routes import home_bp
from app.routes.product_routes import product_bp
from app.routes.auth_routes import auth_bp
from app.utils.errors import APIError
from app.utils.responses import error_response

def create_app():

    app = Flask(__name__)

    init_db()

    CORS(app, resources={
        r"/*": {
            "origins": [
                "http://127.0.0.1:5500",
                "http://localhost:5500",
                "http://localhost:5173",
                "https://product-frontend-psi-five.vercel.app"
            ]
        }
    })

    @app.errorhandler(APIError)
    def handle_api_error(error):
        return error_response(
            error.message,
            error.status_code
        )


    app.register_blueprint(home_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)

    return app