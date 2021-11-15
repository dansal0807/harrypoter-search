from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, Form, SelectField
from wtforms.validators import DataRequired, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entre')
    submit2 = SubmitField('Registre-se')

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor, utilize um nome de usuário diferente.')

class BuscaForms(Form):
    choices = [('name', 'Nome'),
               ('gender', 'Sexo'),
               ('house', 'Casa de Hogwarts'),
               ('actor', 'Ator'),
               ('alternate_names', 'Nomes Alternativos'),
               ('dateOfBirth', 'Data de Nascimento')
               ]
    haystack = SelectField('Escolha o personagem    ', choices=choices)
    needle = StringField('')
