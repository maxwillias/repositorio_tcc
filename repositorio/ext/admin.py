from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import login_required
from werkzeug.security import generate_password_hash
from repositorio.model import db, tcc_artigo, Usuario

# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(sqla.ModelView._handle_view)
admin = Admin()


class UserAdmin(sqla.ModelView):
    column_list = ['nome_completo']
    can_edit = False

    def on_model_change(self, form, model, is_created):
        model.senha = generate_password_hash(model.senha)

def init_app(app):
    admin.init_app(app)
    admin.add_view(sqla.ModelView(tcc_artigo, db.session))
    admin.add_view(sqla.ModelView(Usuario, db.session))
