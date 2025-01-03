from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class QuizForm(FlaskForm):
    q1 = RadioField(
        "Who is often credited with the saying 'I know that I know nothing'?",
        choices=[('1', 'Plato'), ('2', 'Aristotle'), ('3', 'Socrates'), ('4', 'Descartes')],
        validators=[DataRequired()]
    )
    q2 = RadioField(
        "Which philosopher is known for his work 'Meditations on First Philosophy'?",
        choices=[('1', 'John Locke'), ('2', 'René Descartes'), ('3', 'Immanuel Kant'), ('4', 'David Hume')],
        validators=[DataRequired()]
    )
    q3 = RadioField(
        "The concept of 'Übermensch' (Superman) is associated with which philosopher?",
        choices=[('1', 'Karl Marx'), ('2', 'Jean-Paul Sartre'), ('3', 'Friedrich Nietzsche'), ('4', 'Søren Kierkegaard')],
        validators=[DataRequired()]
    )
    q4 = RadioField(
        "Which ancient Greek philosopher founded the school of thought known as Stoicism?",
        choices=[('1', 'Epicurus'), ('2', 'Zeno of Citium'), ('3', 'Pythagoras'), ('4', 'Heraclitus')],
        validators=[DataRequired()]
    )
    q5 = RadioField(
        "Who wrote the philosophical novel 'Thus Spoke Zarathustra'?",
        choices=[('1', 'Jean-Jacques Rousseau'), ('2', 'Arthur Schopenhauer'), ('3', 'Friedrich Nietzsche'), ('4', 'Voltaire')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')