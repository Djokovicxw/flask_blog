from flask_wtf import FlaskForm
from wtforms import fields
from wtforms.validators import DataRequired, Length, InputRequired, Email, EqualTo


class PostForm(FlaskForm):
    id = fields.StringField()
    title = fields.StringField(u'Title', validators=[DataRequired()])
    content = fields.TextAreaField(u'Content', validators=[DataRequired()])
    submit = fields.SubmitField(u'Post')


class LoginForm(FlaskForm):
    username = fields.StringField(u'Username', validators=[DataRequired()])
    password = fields.PasswordField(u'Password', validators=[DataRequired()])
    submit = fields.SubmitField(u'Login')


class RegisterForm(FlaskForm):
    email = fields.StringField(u'Email', validators=[DataRequired(), Email()])
    username = fields.StringField(u'Username', validators=[DataRequired()])
    password = fields.PasswordField(u'Password', validators=[DataRequired(), Length(6, 20)])
    re_password = fields.PasswordField(u'Re-enter password', validators=[EqualTo('password')])
    submit = fields.SubmitField(u'Register')
