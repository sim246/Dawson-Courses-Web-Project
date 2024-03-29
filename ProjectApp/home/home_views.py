from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user
from ..dbmanager import get_db
from werkzeug.security import check_password_hash

from ..users.user import LoginForm

bp = Blueprint('home', __name__, url_prefix="/")


@bp.route('/', methods=['GET', 'POST'])
def login_index():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            user = get_db().get_user(email)
            if user:
                if user.member_type == 'blocked':
                    return render_template('userBlocked.html', form=form)
                # Check password
                pwd = form.password.data
                if check_password_hash(user.password, pwd):
                    remember_me = form.remember_me.data
                    login_user(user, remember=remember_me)
                    return redirect(url_for('courses.list_courses'))
                else:
                    flash("Invalid information")
            else:
                flash("Could not find user")
                redirect(url_for('auth.signup'))
        else:
            flash("Invalid form")
    return render_template('index.html', form=form)


