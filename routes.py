from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, User
from forms import AddUserForm,SignupForm
from passlib.hash import sha256_crypt
from flask_heroku import Heroku

app = Flask(__name__)

# configure connection from flask to postgresql database
#heroku = Heroku(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/final'
#app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://localhost/final'
db.init_app(app)

app.secret_key = "cscie14a-final"

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    #users = Signin.query.all()
    #users = 'test'
    return render_template('index.html', title='Home', users=users)

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = AddUserForm()

    if request.method == 'GET':
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            username = request.form['username']
            password = request.form['password']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            state = request.form['state']
            zipcode = request.form['zipcode']
            age = request.form['age']
            gender = request.form['gender']
            drug_type = request.form['drug_type']
            use_duration = request.form['use_duration']
            med_insurer = request.form['med_insurer']
            year_signed_up = request.form['year_signed_up']
            years_from_first_litigation = request.form['years_from_first_litigation']
            copay_or_coinsurance = request.form['copay_or_coinsurance']
            personal_spending_per_year = request.form['personal_spending_per_year']
            income = request.form['income']
            new_user = User(username=username, password=password, first_name=first_name, last_name=last_name, state=state, zipcode=zipcode, age=age, gender=gender, drug_type=drug_type, use_duration=use_duration, med_insurer=med_insurer, year_signed_up=year_signed_up, years_from_first_litigation=years_from_first_litigation, copay_or_coinsurance=copay_or_coinsurance,personal_spending_per_year=personal_spending_per_year, estimated_opioid_spending_per_year=estimated_opioid_spending_per_year,income=income)
            #new_user = User(username=username, first_name=first_name, last_name=last_name,address=address, city=city, state=state, zipcode=zipcode, insurancetype=insurancetype, age=age)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    form = AddUserForm()
    print(request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None or not sha256_crypt.verify(password, user.password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            session['username'] = username
            return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Login', form=form)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/moreinfo', methods=['POST'])
def moreinfo():
    return render_template('more.html', title='moreinfo')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'username' in session:
        return redirect(url_for('index'))

    form = SignupForm()
    if request.method == 'POST':
        print("this is inside req = post")
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
        existing_user = User.query.filter_by(username=username).first()
        print("this is existing user: ", existing_user)
        if existing_user:
            flash('The username already exists. Please pick another one.')
            return redirect(url_for('signup'))
        else:
            print('add user ....')
            user = User(username=username, password=sha256_crypt.hash(password))
            print(user)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a signuped user!')
            return redirect(url_for('login'))
    else:
        print('this is outside of req =post')
        return render_template('signup.html', title='signup', form=form)
@app.route('/load_data', methods=['GET'])
def load_data():
    users_json = {'users': []}
    users = User.query.all()
    for user in users:
        user_info = user.__dict__
        del user_info['_sa_instance_state']
        users_json['users'].append(user_info)
    return jsonify(users_json)

if __name__ == "__main__":
    app.run(debug=True)
