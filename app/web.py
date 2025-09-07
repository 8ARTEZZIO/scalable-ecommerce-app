"""
Parse input →
call DB/services →
return output as HTML
[ simple Flask routing basically + helper funcs ]
"""
from locale import currency

from flask import Blueprint, flash, render_template, request, redirect, url_for, session
from sqlalchemy.exc import IntegrityError, OperationalError, NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from .extensions import db, login_manager
from .models import User, Product  # add others later (Cart, Orders, etc.)
from .forms import Login, Register, AddProduct

from datetime import date

bp = Blueprint('web', __name__)

@bp.route("/")
def index():
    year = date.today().year
    return render_template("index.html", year=year)

@bp.route("/products", methods=["POST", "GET"])
def products():
    products = db.session.execute(db.select(Product).order_by(Product.name)).scalars()
    return render_template("products.html", products=products)

@bp.route("/product/<name>", methods=["POST", "GET"])
def product(name):
    try:
        product = db.session.execute(db.select(Product).where(Product.name == name)).scalar_one()
    except NoResultFound:
        return redirect(url_for('web.error'))

    return render_template("product.html", product=product)

@bp.route("/product", methods=["GET"])
def get_prod_id():

    if request.method == "GET":
        name = request.args.get("q")
        return redirect(url_for('web.product', name=name))
    else:
        return render_template("index.html")


@bp.route("/error")
def error():
    return render_template("404.html")

@bp.route("/login", methods=["GET", "POST"])
def login():

    form=Login()
    if form.validate_on_submit():

        password = form.password.data
        user = db.session.execute(db.select(User).where(User.username == form.username.data)).scalar()
        db.session.close()

        if not user:
            flash("That username does not exist, please try again.")
            return redirect(url_for('web.login'))
        elif not check_password_hash(user.password_hash, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('web.login'))
        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('web.index'))
    return render_template("login.html", form=form)

@bp.route("/register", methods=["GET", "POST"])
def register():

    error = None
    form = Register()
    if form.validate_on_submit():

        # take user input
        username = form.username.data
        email = form.email.data
        password = form.password.data
        r_pass = form.r_password.data

        # check if username is not taken
        if db.session.execute(db.select(User).where(User.username == username)).scalar():
            flash("This username is already taken.")
            error = True


        # check if email is not taken
        if db.session.execute(db.select(User).where(User.email == email)).scalar():
            flash("This email is in use.")
            error = True

        # check if two passwords are the same
        if password != r_pass:
            error = True
            flash('Passwords must be identical.')

        if not error:
            new_user = User(username=username,
                            email=email,
                            password_hash=generate_password_hash(password),
                            created_at=date.today().strftime("%B %d, %Y")
                            )
            db.session.add(new_user)
            db.session.commit()
            db.session.close()

            flash('Registered successfully!')

    return render_template("signup.html", form=form)

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('web.login'))

@bp.route("/features")
def features():
    return render_template("features.html")

@bp.route("/about")
def about():
    return render_template("about.html")

@bp.route("/profile")
def profile():
    return render_template("profile.html")

@bp.route("/add", methods=["POST", "GET"])
def add_product():

    form = AddProduct()

    if request.method == "POST":
        if not form.validate():
            flash('There was a problem with your submission')
            return render_template('add_product.html', form=form)
        else:
            product = Product(
                name=form.name.data,
                slug=form.slug.data,
                price=form.price.data,
                currency=form.currency.data,
                description=form.description.data,
                main_image_url=form.image_url.data,
                stock=form.stock.data,
                is_active=form.active.data,
                created_at=date.today().strftime("%B %d, %Y")
            )

            db.session.add(product)
            db.session.commit()
            db.session.close()

            flash(f'Successfully added a new product: {form.name.data}')

    recent = db.session.execute(db.select(Product).order_by(Product.name)).scalars()
    db.session.close()

    return render_template("add_product.html", recent=recent, form=form)

