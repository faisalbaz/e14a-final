from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, EqualTo

class AddUserForm(FlaskForm):
    #username = StringField('Username (Email)', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    state = SelectField('State', validators=[DataRequired()], choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])
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
