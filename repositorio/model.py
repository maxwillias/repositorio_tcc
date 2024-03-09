from repositorio.ext.database import db, Integer, String, Column
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash

class tcc_artigo(db.Model, SerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    tipo = Column(String, nullable=False)
    orientador = Column(String, nullable=False)
    data_apresentacao = Column(String, nullable=False)

    def __init__(self, titulo, autor, tipo, orientador, data_apresentacao):
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.orientador = orientador
        self.data_apresentacao = data_apresentacao

class Usuario(db.Model, SerializerMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_completo = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)

    def __init__(self, nome_completo, senha, data_nascimento):
        self.nome_completo = nome_completo
        self.senha = generate_password_hash(senha)
        self.data_nascimento = data_nascimento


def get_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()