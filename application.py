from flask import Flask

def create_app(app_name='SURVEY_API'):
    app = Flask(app_name)
    app.config.from_object('config.BaseConfig')
    from api import api
    app.register_blueprint(api, url_prefix="/api")

    from models import db
    db.init_app(app)
    return app