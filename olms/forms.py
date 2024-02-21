from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from olms.models import User, Course


class RegisterForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for user registration
    
    # custom validation methods
    
    def validate_username(self, username_to_check):
        # Checks if the username already exists in the database.
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists try another one!')
        
    def validate_email_address(self, email_address_to_check):
        # Checks if the email address already exists in the database.
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address already exists, try another one!')

    username = StringField(label='User Name:', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for a user to login
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class CourseForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for course to be created
    name = StringField(label='Course Name', validators=[DataRequired()])
    duration_in_month = IntegerField(label='Duration (months)', validators=[DataRequired()])
    payment = IntegerField(label='Payment', validators=[DataRequired()])
    description = TextAreaField(label='Description', validators=[DataRequired()])
    submit = SubmitField(label='Add Course')


class AdminRegisterForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for an Admin to register
    username = StringField(label='Admin User Name:', validators=[Length(min=3, max=30), DataRequired()])
    email_address = StringField(label='Admin Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Admin Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Admin Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Admin Account')


class AdminLoginForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for an admin to login
    username = StringField(label='Admin User Name:', validators=[DataRequired()])
    password = PasswordField(label='Admin Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in as Admin')


class PurchaseCourseForm(FlaskForm):
    # a class that inherits from FlaskForm and defines a form for a user to enroll in a course
    purchased_course = SelectField('Select Course', validators=[DataRequired()], coerce=int)
    submit = SubmitField(label='Enroll Now')
