from flask import render_template, request, url_for, redirect
from repositorio import model
from repositorio.model import db, tcc_artigo, Usuario

def init_app(app):
    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/login", view_func=login)
    app.add_url_rule("/cadastro_tcc_artigo", view_func=cadastro_tcc_artigo, methods =['GET','POST'])
    app.add_url_rule("/cadastro", view_func=cadastro, methods =['GET','POST'])
    app.add_url_rule("/listar_tcc_artigo", view_func=listar_tcc_artigo)

def index():
    return render_template("index.html")

def login():
    
    return render_template("login.html")

def cadastro_tcc_artigo():
    if request.method == 'POST':

        arquivo = tcc_artigo(request.form['titulo'],request.form['autor'],request.form['tipo'],request.form['orientador'],request.form['data_apresentacao'])
        db.session.add(arquivo)
        db.session.commit()
        return redirect(url_for("listar_tcc_artigo"))

    return render_template("cadastro_tcc_artigo.html")

def cadastro():
    if request.method == 'POST':

        usuario = Usuario(request.form['nome_completo'],request.form['senha'],request.form['data_nascimento'])
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for("cadastro_tcc_artigo"))

    return render_template("cadastro.html")

def listar_tcc_artigo():

    h = model.tcc_artigo.query.all()

    return render_template("listar_tcc_artigo.html", tcc_artigo=h)