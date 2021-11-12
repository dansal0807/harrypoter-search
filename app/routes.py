from flask import render_template, redirect, flash, url_for
from app import app, db
from app.forms import LoginForm, FlaskForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from app.forms import RegistrationForm
import requests 
import json

#renderização das rotas do formulário:
@app.route('/')
@app.route('/index')
@login_required
def index():
    form = LoginForm()
    return render_template('login.html', title='Cadastre-se', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos.')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Cadastre-se', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Agora você está registrado!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    buscas = [
        {'usuário': user, 'busca': 'Test post #1'},
        {'usuário': user, 'busca': 'Test post #2'}
    ]    
    return render_template('user.html', user=user, buscas=buscas)

@app.route('/busca')
@login_required
def busca():
    return render_template('busca.html')


