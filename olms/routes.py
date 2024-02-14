from olms import app
from flask import render_template, redirect, url_for, flash, request
from olms.models import Course, User
from olms.forms import RegisterForm, LoginForm, PurchaseCourseForm
from olms import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home():
    """ simply return hello world """
    return render_template("home.html")


@app.route("/graphic_design")
def graphic_design():
    return "<h1>welcome to the graphic design page</h1>"


@app.route("/web_development")
def web_development():
    return "<h1>welcome to the web development page</h1>"


@app.route("/video_editing")
def video_editing():
    return "<h1>welcome to the video editing page</h1>"


@app.route("/digital_marketing")
def digital_marketing():
    return "<h1>welcome to the digital marketing page</h1>"


@app.route("/enrollment", methods=['GET', 'POST'])
@login_required
def enroll():
    """ returns the enrollment details """
    purchase_form = PurchaseCourseForm()
    if request.method == "POST":
        purchased_course = request.form.get('purchased_course')
        p_course_object = Course.query.filter_by(name=purchased_course).first()
        if p_course_object:
            if current_user.can_purchase(p_course_object):
                p_course_object.buy(current_user)
                flash(f"Congratulations! You purchased {p_course_object.name} for {p_course_object.payment}$", category='success')
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_course_object.name}!", category='danger')

        if p_course_object.name == "Graphics Design":
            return redirect(url_for('graphic_design'))
        
        if p_course_object.name == "Web Development":
            return redirect(url_for('web_development'))
        
        if p_course_object.name == "Video Editing":
            return redirect(url_for('video_editing'))
        
        if p_course_object.name == "Digital Marketing":
            return redirect(url_for('digital_marketing'))

        else:
            return redirect(url_for('home'))
    if request.method == "GET":
        courses = Course.query.all()
        return render_template("enroll.html", courses=courses, purchase_form=purchase_form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    """ a route to register a user"""
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Created Account Successfully! You are logged in as: {user_to_create.username}', category='success')
        return redirect(url_for('enroll'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'there is an error creating the user: {err_msg}', category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('enroll'))
        else:
            flash('Username and Password does not exist, please try again', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("you have been logged out!", category="info")
    return redirect(url_for("home"))