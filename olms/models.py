from olms import db, login_manager
from olms import bcrypt
from flask_login import UserMixin

# a decorator used to register a function that loads a users from a database based on user's id
@login_manager.user_loader
def load_user(user_id):
    # a function that takes user id as an argument and used for loading user object
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    # inherits from db.Model, indicating that it's a model class mapped to a database table.
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=0)
    courses= db.relationship('Course', backref='enrolled_user', lazy=True)

    # formats the budget attribute to make it more readable.
    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    # a property getter method that returns the password hash.
    @property
    def password(self):
        return self.password

    # hashes the plain text password using bcrypt and sets the hashed password to the password_hash attribute.
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        # checks if the provided password matches the hashed password stored in the database.
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def can_purchase(self, course_obj):
        # checks if the user's budget is sufficient to purchase a given course based on its payment amount.
        return self.budget >= course_obj.payment
    

class Admin(db.Model, UserMixin):
    # inherits from db.Model, indicating that it's a model class mapped to a database table.
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=50), nullable=False)

    # a property getter method that returns the password hash.
    @property
    def password(self):
        return self.password_hash

    # hashes the plain text password using bcrypt and sets the hashed password to the password_hash attribute.
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        # checks if the provided password matches the hashed password stored in the database.
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Course(db.Model):
    # inherits from db.Model, indicating that it's a model class mapped to a database table.
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    duration_in_month = db.Column(db.Integer(), nullable=False)
    payment = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    student = db.Column(db.Integer(), db.ForeignKey('user.id'))

    # used to represent the courses in a dictionary form
    def __repr__(self):
        return f'Course {self.name}'
    
    def buy(self, user):
        # a method used to purchase a course
        self.student = user.id
        user.budget -= self.payment
        db.session.commit()
