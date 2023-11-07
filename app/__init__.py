from flask import Flask
from app.extensions import db
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    # Register blueprints here
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp,url_prefix='/')
    
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp,url_prefix='/auth')
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.register import bp as register_bp
    app.register_blueprint(register_bp, url_prefix='/register')
    
    
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app