def init_app(app):
    app.config["TITLE"]="Repositório Institucional"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mvc.db"
    app.config['SECRET_KEY'] = 'something-secret'
    app.config['SIMPLELOGIN_LOGIN_URL'] = '/login/'
    app.config['SIMPLELOGIN_LOGOUT_URL'] = '/exit/'