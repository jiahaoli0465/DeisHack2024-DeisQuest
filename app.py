import os
import openai


from flask import Flask, render_template, request, flash, redirect, session, g, url_for, jsonify
app = Flask(__name__)

app.app_context().push()

from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from forms import RegisterForm, LoginForm, EditWorkLog, NewExercise, NewWorkLog,NewWorkType
from models import db, connect_db, User, Worklog, WorkoutType, Exercise, ExerciseSet, WorkoutExercise

# from assistant.assistant import assistantbot, client


# app.register_blueprint(assistantbot)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///IBSquest'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()

db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def show_home():
    users = User.query.all()
    # if 'thread_id' not in session:
        # thread = client.beta.threads.create()
        # session['thread_id'] = thread.id
    return render_template('home.html', users = users)

@app.route('/quests')
def quest_page():
    return render_template('tasks.html')

@app.route('/rewards')
def rewards_page():
    return render_template('rewards.html')

@app.route('/rankings')
def rankings_page():
    return render_template('ranking.html')

@app.route('/newsletter')
def newsletter_page():
    return render_template('newsletter.html')

@app.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def show_dashboard():
    worklogs = Worklog.query.filter_by(user_id=current_user.id).all()
    return render_template('users/dashboard.html', worklogs = worklogs)
    




#####################################################
# Login/Register for users

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        login_user(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


    
@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            login_user(user)
            flash('Logged in successfully.', category='success')
            # next = request.args.get('next')
            return redirect("/")

        else:
            form.username.errors = ["Invalid input"]
            return render_template("users/login.html", form=form)

    else:
        return render_template("users/login.html", form=form)
    
@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#End login/ Register Routes
#####################################################

    

