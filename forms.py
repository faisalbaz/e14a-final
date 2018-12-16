from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class AddUserForm(FlaskForm):
    #username = StringField('Username (Email)', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    gender = SelectField('Copay or Co-Insurance', validators=[DataRequired()], choices=[('M', 'Male'), ('F', 'Female')])
    drug_type = SelectField('Drug Type', validators=[DataRequired()], choices=[('AMPHETAMINE', 'Amphetamine'), ('CODEINE', 'Codeine'), ('GAMMA HYDROXYBUTYRIC ACID', 'Gamma Hydroxybutyric Acid'), ('HYDROCODONE', 'Hydrocodone'), ('LISDEXAMFETAMINE', 'Lisdexamfetamine'), ('METHADONE', 'Methadone'), ('METHYLPHENIDATE', 'Methylphenidate'), ('MORPHINE', 'Morphine'), ('OXYCODONE', 'Oxycodone'), ('PENTOBARBITAL', 'Pentobarbital'), ('TAPENTADOL', 'Tapentadol'), ('Other', 'Other')])
    use_duration = FloatField('Years of Use', validators=[DataRequired()])
    med_insurer = SelectField('Copay or Co-Insurance', validators=[DataRequired()], choices=[('Medicaid', 'Medicaid'), ('Medicare', 'Medicare'), ('Other', 'Other')])
    year_signed_up = IntegerField('Year Insured', validators=[DataRequired()])
    years_from_first_litigation = FloatField('Years Since Start of Litigation', validators=[DataRequired()])
    copay_or_coinsurance = SelectField('Copay or Co-Insurance', validators=[DataRequired()], choices=[('copay', 'Copay'), ('coinsurance', 'Co-Insurance')])
    personal_spending_per_year = FloatField('How much do you spend per year?', validators=[DataRequired()])
    income = FloatField('Annual Income', validators=[DataRequired()])
    submit = SubmitField('Submit')
class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Signup')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
