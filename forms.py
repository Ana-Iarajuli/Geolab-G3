from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, DateField,
                            IntegerField, RadioField, SelectField, SubmitField)
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    username = StringField("შეიყვანე სახელი", validators=[
                            DataRequired()])
    password = PasswordField("შეიყვანე პაროლი", validators=[DataRequired(), length(min=8, max=64, message="მინიმალური ზომა 8 სიმბოლოა")])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("password",
                                                                                             message="პაროლები უნდა ემთხვეოდეს")])

    register_button = SubmitField()


class LoginForm(FlaskForm):
    username = StringField("შეიყვანე სახელი")
    password = PasswordField("შეიყვანე პაროლი")

    login_button = SubmitField()


class MovieForm(FlaskForm):
    name = StringField("შეიყვანე ფილმის სახელი")
    release_year = IntegerField("შეიყვანე გამოშვების წელი")
    image = FileField("ატვირთე ფილმის ფოტო")

    button = SubmitField("დაამატე ფილმი")