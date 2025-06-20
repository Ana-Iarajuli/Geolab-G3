from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, DateField,
                            IntegerField, RadioField, SelectField, SubmitField)
from wtforms.validators import DataRequired, length, equal_to
from flask_wtf.file import FileField, FileSize, FileAllowed, FileRequired


class RegisterForm(FlaskForm):
    image = FileField("ატვირთე პროფილის ფოტო", validators=[FileRequired(),
        FileSize(4, message="ფაილის ზომა მაქსიმუმ 4მბ"),
        FileAllowed([".jpg", ".png", ".jpeg"])
    ])
    username = StringField("შეიყვანე სახელი", validators=[
                            DataRequired()])
    password = PasswordField("შეიყვანე პაროლი", validators=[DataRequired(), length(min=8, max=64, message="მინიმალური ზომა 8 სიმბოლოა")])
    confirm_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("password",
                                                                                             message="პაროლები უნდა ემთხვეოდეს")])
    birthdate = DateField()
    mobile_number = IntegerField("+995 555 55 55", validators=[DataRequired()])
    gender = RadioField("აირჩიე სქესი", choices=["ქალი", "კაცი", "კატა"], validators=[DataRequired()])
    country = SelectField(choices=["ვისი გორისა ხარ?", "საქართველო", "იაპონია", "ზიმბაბვე"], validators=[DataRequired()])

    register_button = SubmitField()


class MovieForm(FlaskForm):
    name = StringField("შეიყვანე ფილმის სახელი")
    release_year = IntegerField("შეიყვანე გამოშვების წელი")
    image = FileField("ატვირთე ფილმის ფოტო")

    button = SubmitField("დაამატე ფილმი")