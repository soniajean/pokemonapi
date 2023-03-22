from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class SignUpForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
<<<<<<< HEAD
    confirm_password = PasswordField('Confirm', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()



=======
    confirm_password = PasswordField("Confirm", validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()
>>>>>>> 931548056e8b0465b13bfc4ef7f04fed0ba2fdfa
