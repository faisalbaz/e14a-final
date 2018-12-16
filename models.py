from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(64), nullable=False)
    drug_type = db.Column(db.String(64), nullable=False)
    zipcode = db.Column(db.String(64), nullable=False)
    state = db.Column(db.String(64), nullable=False)
    use_duration = db.Column(db.Float, nullable=False)
    med_insurer = db.Column(db.String(64), nullable=False)
    year_signed_up = db.Column(db.Integer, nullable=False)
    years_from_first_litigation = db.Column(db.Float, nullable=False)
    copay_or_coinsurance = db.Column(db.String(64), nullable=False)
    personal_spending_per_year = db.Column(db.Float, nullable=False)
    total_spending = db.Column(db.Float, nullable=False)
    income = db.Column(db.Float, nullable=False)