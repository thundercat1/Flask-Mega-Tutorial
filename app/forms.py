from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    openid = StringField('openid', validators =[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class ProfileEditForm(Form):
    nickname = StringField('Nickname', validators=[DataRequired()])
    about_me = TextAreaField('About Me', validators=[Length(min=0, max=120)])
