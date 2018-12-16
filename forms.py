from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class AddUserForm(FlaskForm):
    username = StringField('Username (Email)', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender =  StringField('Gender', validators=[DataRequired()])
    drug_type = StringField('Drug Type', validators=[DataRequired()])
    use_duration = FloatField('Years of Use', validators=[DataRequired()])
    med_insurer = StringField('Insurance Type', validators=[DataRequired()])
    year_signed_up = IntegerField('Year Insured', validators=[DataRequired()])
    years_from_first_litigation = FloatField('Years Since Start of Litigation', validators=[DataRequired()])
    copay_or_coinsurance = FloatField('Copay or Co-Insurance', validators=[DataRequired()])
    personal_spending_per_year = FloatField('How much do you spend per year?', validators=[DataRequired()])
    income = FloatField('Annual Income', validators=[DataRequired()])
    submit = SubmitField('Add')
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Signup')
