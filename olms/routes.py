from olms import app
from flask import render_template, redirect, url_for, flash, request
from olms.models import Course, User, Admin
from olms.forms import RegisterForm, LoginForm, PurchaseCourseForm, CourseForm, AdminLoginForm, AdminRegisterForm
from olms import db
from flask_login import login_user, logout_user, login_required, current_user

# routes defined here

@app.route("/")
@app.route("/home")
def home():
    """ serves a home page """
    return render_template("home.html")


@app.route("/about")
def about():
    """ serves an about page """
    return render_template("about.html")


@app.route("/enrollment/graphic_design")
def graphic_design():
    """ serves the page for graphic design content """
    return render_template("graphics_design.html")


@app.route("/enrollment/web_development")
def web_development():
    """ serves the page for web development content """
    return render_template("web_development.html")


@app.route("/enrollment/video_editing")
def video_editing():
    """ serves the page for video editing content """
    return render_template("video_editing.html")


@app.route("/enrollment/digital_marketing")
def digital_marketing():
    """ serves the page for digital marketing content """
    return render_template("digital_marketing.html")


@app.route('/admin/courses', methods=['GET', 'POST'])
def admin_courses():
    """ a route used to define a page to manage courses for Adminstrator """
    form = CourseForm()
    if request.method == 'POST':
        course = Course(name=form.name.data,
                        duration_in_month=form.duration_in_month.data,
                        payment=form.payment.data,
                        description=form.description.data)
        db.session.add(course)
        db.session.commit()
        flash(f'Created Course Successfully! {course.name}', category='success')
        return redirect(url_for('admin_courses'))
    courses = Course.query.all()
    return render_template('admin_courses.html', form=form, courses=courses)


@app.route('/admin/courses/delete/<int:course_id>', methods=['POST'])
def delete_course(course_id):
    """ a route that allow the Adminstrator to delete a course """
    if request.method == 'POST':
        course = Course.query.get_or_404(course_id)
        db.session.delete(course)
        db.session.commit()
        flash(f'Deleted Course Successfully! {course.name}', category='success')
    return redirect(url_for('admin_courses'))


@app.route("/enrollment", methods=['GET', 'POST'])
@login_required
def enroll():
    """ a route that returns the enrollment details lists of courses """
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
    """ a route to register or sign up a user"""
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
    """ a route used to login to user """
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


# In routes.py
@app.route("/admin/register", methods=['GET', 'POST'])
def admin_register():
    """ a route to register an admin"""
    form = AdminRegisterForm()
    if form.validate_on_submit():
        admin_to_create = Admin(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(admin_to_create)
        db.session.commit()
        login_user(admin_to_create)
        flash(f'Created Admin Account Successfully! You are logged in as: {admin_to_create.username}', category='success')
        return redirect(url_for('admin_courses'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'there is an error creating the admin: {err_msg}', category='danger')
    return render_template('admin_register.html', form=form)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """ a route that serves the admin login page"""
    form = AdminLoginForm()
    if form.validate_on_submit():
        attempted_admin = Admin.query.filter_by(username=form.username.data).first()
        if attempted_admin and attempted_admin.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_admin)
            flash(f'Success! You are logged in as admin: {attempted_admin.username}', category='success')
            return redirect(url_for('admin_courses'))
        else:
            flash('Username and Password does not exist, please try again', category='danger')
    return render_template('admin_login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """ a route used to olgout the the user and the admin """
    logout_user()
    flash("you have been logged out!", category="info")
    return redirect(url_for("home"))
