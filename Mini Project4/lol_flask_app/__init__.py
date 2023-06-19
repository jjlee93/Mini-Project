from flask import Flask

def create_app():
    app = Flask(__name__)
    app.static_folder = 'static'
    
    # 블루프린트 등록
    from .views.search import home_bp
    from .views.prediction import prediction_bp
    from .views.result import result_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(prediction_bp)
    app.register_blueprint(result_bp)
    
    return app