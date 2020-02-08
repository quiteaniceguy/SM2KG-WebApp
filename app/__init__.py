from flask import Flask
from config import Config

def create_app(config_class=Config): 
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class) 
    from app.giturl_class import bp as giturl_class_bp
    flask_app.register_blueprint(giturl_class_bp)

    print("flask app created")

    return flask_app



