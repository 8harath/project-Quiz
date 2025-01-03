from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Quiz
from forms import LoginForm, RegistrationForm, QuizForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///philosophy_quiz.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('quiz'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    form = QuizForm()
    if form.validate_on_submit():
        score = calculate_score(form)
        new_quiz = Quiz(user_id=current_user.id, score=score)
        db.session.add(new_quiz)
        db.session.commit()
        return redirect(url_for('results'))
    return render_template('quiz.html', form=form)

@app.route('/results')
@login_required
def results():
    latest_quiz = Quiz.query.filter_by(user_id=current_user.id).order_by(Quiz.id.desc()).first()
    return render_template('results.html', quiz=latest_quiz)

# ... (previous code remains the same)

def calculate_score(form):
    correct_answers = {
        'q1': '3',  # Socrates
        'q2': '2',  # René Descartes
        'q3': '3',  # Friedrich Nietzsche
        'q4': '2',  # Zeno of Citium
        'q5': '3'   # Friedrich Nietzsche
    }
    score = sum(1 for q, a in correct_answers.items() if getattr(form, q).data == a)
    return score

# ... (rest of the code remains the same)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)