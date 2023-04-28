from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

from .models import Comment


class LoginForm(FlaskForm):
    username = StringField("Логин", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])


class CommentForm(FlaskForm):
    text = StringField("Комментарий", validators=[DataRequired()])
    