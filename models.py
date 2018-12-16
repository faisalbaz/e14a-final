from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(128), nullable=True)
    first_name = db.Column(db.String(64), nullable=True)
    last_name = db.Column(db.String(64), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(64), nullable=True)
    drug_type = db.Column(db.String(64), nullable=True)
    zipcode = db.Column(db.String(64), nullable=True)
    state = db.Column(db.String(64), nullable=True)
    use_duration = db.Column(db.Float, nullable=True)
    med_insurer = db.Column(db.String(64), nullable=True)
    year_signed_up = db.Column(db.Integer, nullable=True)
    years_from_first_litigation = db.Column(db.Float, nullable=True)
    copay_or_coinsurance = db.Column(db.String(64), nullable=True)
    personal_spending_per_year = db.Column(db.Float, nullable=True)
    total_spending = db.Column(db.Float, nullable=True)
    income = db.Column(db.Float, nullable=True)