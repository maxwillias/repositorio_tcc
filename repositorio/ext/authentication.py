from flask_simplelogin import SimpleLogin
from werkzeug.security import check_password_hash, generate_password_hash
from repositorio.model import db, Usuario

def verify_login(username, password):
    """Valida o usuario e senha para efetuar o login"""
    
    if not username or not password:
        return False
    existing_user = Usuario.query.filter_by(nome_completo=username).first()

    if not existing_user:
        return False
    if check_password_hash(existing_user.senha, password):
        return True
    return False

def init_app(app):
    SimpleLogin(app, login_checker=verify_login)
