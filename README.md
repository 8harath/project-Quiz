# Philosophy Quiz Web Application
## 3rd Semester Computer Science Undergraduate Project

A Flask-based web application developed as part of my third-semester Computer Science undergraduate coursework. This project demonstrates the implementation of web development concepts including user authentication, database management, and interactive quiz functionality.

## 🎓 Academic Context

This project was developed as part of the third-semester curriculum in Computer Science, focusing on:
- Web Application Development
- Database Management
- User Interface Design
- Security Implementation
- Full-Stack Development

## 💻 Code Structure and Implementation Details

### Backend Implementation (`app.py`)
```python
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///philosophy_quiz.db'
```
The application uses Flask as the web framework and SQLite as the database. Key implementations include:

1. **User Authentication System**
   ```python
   @app.route('/login', methods=['GET', 'POST'])
   def login():
       form = LoginForm()
       if form.validate_on_submit():
           user = User.query.filter_by(username=form.username.data).first()
   ```
   - Implements secure login using Flask-Login
   - Handles password hashing via Werkzeug
   - Manages user sessions

2. **Quiz Logic**
   ```python
   def calculate_score(form):
       correct_answers = {
           'q1': '3',  # Socrates
           'q2': '2',  # René Descartes
           # ...
       }
   ```
   - Implements score calculation
   - Tracks user responses
   - Stores quiz results in database

### Database Models (`models.py`)
The application uses SQLAlchemy ORM with two main models:

1. **User Model**
```python
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
```
- Handles user data storage
- Implements UserMixin for Flask-Login functionality
- Manages relationships with quiz attempts

2. **Quiz Model**
```python
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
```
- Records quiz attempts
- Links to user through foreign key
- Stores timestamps and scores

### Form Handling (`forms.py`)
Implements WTForms for secure form handling:

1. **Authentication Forms**
```python
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
```
- Implements form validation
- Handles user input sanitization
- Manages password confirmation

2. **Quiz Form**
```python
class QuizForm(FlaskForm):
    q1 = RadioField(
        "Who is often credited with the saying 'I know that I know nothing'?",
        choices=[('1', 'Plato'), ('2', 'Aristotle'), ('3', 'Socrates'), ('4', 'Descartes')],
        validators=[DataRequired()]
    )
```
- Implements multiple choice questions
- Handles answer validation
- Manages quiz submission

### Frontend Implementation

1. **Template Structure**
```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Philosophy Quiz{% endblock %}</title>
</head>
```
- Uses Jinja2 templating
- Implements template inheritance
- Manages dynamic content rendering

2. **Responsive Design (`style.css`)**
```css
.navbar {
    background-color: var(--header-color);
    color: #fff;
    padding: 1rem 0;
}
```
- Implements mobile-first design
- Uses CSS variables for consistency
- Manages responsive layouts

## 🔧 Technical Implementation

### Authentication Flow
1. User registration
   - Password hashing
   - Username validation
   - Database entry creation

2. Login process
   - Credential verification
   - Session management
   - Secure routing

### Quiz Implementation
1. Question presentation
   - Random ordering
   - Answer validation
   - Score calculation

2. Result management
   - Score storage
   - History tracking
   - Performance visualization

## 📚 Learning Outcomes

This project demonstrated proficiency in:
- Flask web framework implementation
- Database design and management
- User authentication systems
- Frontend-backend integration
- Responsive web design
- Form handling and validation
- Security best practices

## 🚀 Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/philosophy-quiz.git
cd philosophy-quiz
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize database:
```bash
python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

4. Run the application:
```bash
python app.py
```

## 🤝 Contributing

This is an academic project, but contributions are welcome. Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

Bharath K - Computer Science Undergraduate
- GitHub: 8harath (https://github.com/8harath)
- Academic Institution: Jain University
- Course: Web Development (CS-001)
- Semester: 3rd Semester, 2024

## 🙏 Acknowledgments

- Course Instructor: Santhalakshmi 
- Flask Documentation and Community
- SQLAlchemy Documentation
- Academic Resources and References
