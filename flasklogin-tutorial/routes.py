"""Routes for logged-in flask_session_tutorial."""
from flask import Blueprint, redirect, render_template, session, url_for, request, make_response
from flask import current_app as app
from flask_login import current_user, login_required, logout_user
from .assets import compile_auth_assets
from datetime import datetime as dt
from .models import db, User

# Blueprint Configuration
main_bp = Blueprint(
    "main_bp", __name__,
    template_folder="templates",
    static_folder="static"
)


@main_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    """Logged in Dashboard screen."""
    session["redis_test"] = "This is a session variable."
    return render_template(
        "dashboard.jinja2",
        title="Flask-Session Tutorial.",
        template="dashboard-template",
        current_user=current_user,
        body="You are now logged in!",
    )


@main_bp.route("/session", methods=["GET"])
@login_required
def session_view():
    """Display session variable value."""
    return render_template(
        "session.jinja2",
        title="Flask-Session Tutorial.",
        template="dashboard-template",
        session_variable=str(session["redis_test"]),
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for("auth_bp.login"))

@app.route('/', methods=['GET'])
def user_records():
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="Robert Deniro's first movie was in 1988",
            admin=False
        )
        db.session.add(new_user)
        db.session.commit()
    return make_response(f"{new_user}successfully created!")

@app.route('/', methods=['GET'])
def create_user():

@app.route('/', methods=['GET'])
def user_records():
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        if existing_user:
            return make_response(
                f'{username} ({email}) already created!'
            )
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            bio="Robert Deniro's first movie was in 1988",
            admin=False
        )
        db.session.add(new_user)
        db.session.commit()
        redirect(url_for('user_records'))

    return render_template(
        'users.jinja2',
        users=User.query.all(),
        title="Show Users"
    )

