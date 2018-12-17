from flask import Flask, flash, render_template, request, url_for, redirect, jsonify, session
from models import db, User
from sklearn.externals import joblib
from forms import AddUserForm,SignupForm, LoginForm
from passlib.hash import sha256_crypt
import numpy as np
import pickle
from utils import onehotCategorical, onehotState
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
    #users = User.query.all()
    if 'username' in session:
        session_user = User.query.filter_by(username=session['username']).first()
        return render_template('index.html', title='Home', session_username=session_user.username)
        #posts=followed_posts,, max_post=max_post
    else:
        # all_posts = Post.query.all()
        # max_post = db.session.query(func.max(Post.pid)).scalar()
        return render_template('index.html', title='Home')


@app.route('/add_user/<username>', methods=['GET', 'POST'])
def add_user(username):
    form = AddUserForm()
    #session_user = User.query.filter_by(username=session['username']).first()
    session_user = User.query.filter(User.username == username).first()
    if request.method == 'GET':
        return render_template('add_user.html', form=form, title='Add User Information', session_username=session_user.username)
    else:
        #session_user.first_name= 'first_name'
        #session_user.last_name= 'last_name'
        #db.session.commit()
        #return redirect('/index')
        #session_user = User.query.filter_by(username=session['username']).first()
        if form.validate_on_submit():
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
<<<<<<< HEAD
            if copay_or_coinsurance == 'copay':
                total_spending = float(personal_spending_per_year)/.11
            else:
                total_spending = float(personal_spending_per_year)/.15
            #return total_spending
            session_user.first_name= first_name
            session_user.last_name= last_name
            session_user.state= state
            session_user.zipcode= zipcode
            session_user.age= age
            session_user.gender= gender
            session_user.drug_type= drug_type
            session_user.use_duration= use_duration
            session_user.med_insurer= med_insurer
            session_user.year_signed_up= year_signed_up
            session_user.years_from_first_litigation= years_from_first_litigation
            session_user.copay_or_coinsurance= copay_or_coinsurance
            session_user.personal_spending_per_year= personal_spending_per_year
            session_user.total_spending=total_spending
            session_user.income= income

            if gender == "M":
                gender_1hot = np.array([0, 1])
            else:
                gender_1hot = np.array([1, 0])

            state_1hot = onehotState(state)

            years_int = int(years_from_first_litigation)
            years_1hot= onehotCategorical(years_int, 20)
            print(state_1hot)
            #test_pred = np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 36, 56361, 305.5437079])
            #test_pred = np.hstack([gender_1hot, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], years_1hot, [age, income, total_spending]])
            test_pred = np.hstack([gender_1hot, state_1hot, years_1hot, [age, income, total_spending]])
            #prediction = model.predict(test_pred.reshape(1, -1))*473.5694972
            prediction = model.predict(test_pred.reshape(1, -1))*total_spending
            session_user.est_settle = float(np.squeeze(prediction.round(2)))
            #settle = "$" + str(np.squeeze(prediction.round(2)))
=======
            new_user = User(username=username, password=password, first_name=first_name, last_name=last_name, state=state, zipcode=zipcode, age=age, gender=gender, drug_type=drug_type, use_duration=use_duration, med_insurer=med_insurer, year_signed_up=year_signed_up, years_from_first_litigation=years_from_first_litigation, copay_or_coinsurance=copay_or_coinsurance,personal_spending_per_year=personal_spending_per_year, income=income)
            #new_user = User(username=username, first_name=first_name, last_name=last_name,address=address, city=city, state=state, zipcode=zipcode, insurancetype=insurancetype, age=age)
            db.session.add(new_user)
>>>>>>> 0d0b778fd602c505ed0c36e410f4d09b491af988
            db.session.commit()
            #return redirect('/index')
            return redirect(url_for('profile', username=session_user.username))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))

    form = LoginForm()
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
        elif not password == password2:
            flash('Password do not match.')
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

@app.route('/profile/<username>', methods=['POST', 'GET'])
def profile(username):
    # test_pred = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 51331, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 473.5694972, 0, 0, 0, 1, 0, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # prediction = model.predict(test_pred.reshape(1, -1))*473.5694972
    # settle = "$" + str(np.squeeze(prediction.round(2)))
    if 'username' in session:
        user = User.query.filter_by(username=username).first_or_404()

        # condos_liked = Like.query.filter_by(liker_id=user.uid).all()
        # conids_liked = [f.likedcon_id for f in condos_liked]
        # liked_condos = Condo.query.filter(Condo.conid.in_(conids_liked)).all()
        #posts = Post.query.filter_by(author=user.uid).all()
        return render_template('profile.html', title='Profile', user=user, session_username=user.username)
    else:
        #return render_template('profile.html', title='Profile', user=user, settle=settle)
        return redirect(url_for('index'))

@app.route('/test')
def test():
    if 'username' in session:
        session_user = User.query.filter_by(username=session['username']).first()
        return render_template('test.html', title='Test', session_username=session_user.username)
    else:
        return render_template('test.html', title='Test')



if __name__ == "__main__":
    # load ML model
    model = joblib.load('rm.pkl')
    app.run(debug=True)
