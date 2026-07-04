from flask import Flask
from flask_cors import CORS
from config import Config
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    db.init_app(app)
    
    with app.app_context():
        # Khởi tạo database tables nếu chưa có
        db.create_all()
        
    # Register Blueprints
    from routes.auth import auth_bp
    from routes.room import room_bp
    from routes.resident import resident_bp
    from routes.dashboard import dashboard_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(room_bp, url_prefix='/api/rooms')
    app.register_blueprint(resident_bp, url_prefix='/api/residents')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
        
    @app.route('/api')
    def index():
        return {"message": "Mini Apartment Management API is running!"}
        
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
