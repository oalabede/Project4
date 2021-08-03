from flask_login import current_user, login_required, logout_user
from datetime import datetime as dt
from flask import Blueprint, redirect, render_template, session, url_for, request, make_response, Flask, g
from flask import current_app as app
from .forms import ContactForm


app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html", title='Flask-Login Tutorial.', body="You are now logged in!")

app = Flask(__name__)
@app.route("/api/v2/test_response")
def users():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        headers=headers
    )

@app.route("/login")
def login():
    return redirect('/dashboard.html')


@app.route("/login")
def login():
    return redirect(url_for('dashboard'))


app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard 'contact' form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2",
        form=form,
        template="form-template"
    )

main_bp = Blueprint(
    "main_bp", __name__,
    template_folder="templates",
    static_folder="static"
)


@main_bp.route("/", methods=["GET"])
@login_required
def dashboard(current_user=None):
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
def user_records(db=None):
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


class User:
    pass


@app.route('/', methods=['GET'])
def user_records(db=None):
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

def get_test_value():
    if 'test_value' not in g:
        g.test_value = 'This is a value'
    return g.test_value

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(render_template("404.html"), 404)

@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(render_template("400.html"), 400)

@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(render_template("500.html"), 500)