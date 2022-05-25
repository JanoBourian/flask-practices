from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name? ', validators=[DataRequired()])
    role = SelectField('Role', validators=[DataRequired()])
    submit = SubmitField('Submit')