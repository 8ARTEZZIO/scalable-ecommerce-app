from flask import Blueprint, flash, render_template, request, redirect, url_for, session, jsonify, abort
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps

from .extensions import db, login_manager
from .models import User, Product  # add others later (Cart, Orders, etc.)
from .forms import Login, Register, AddProduct

from datetime import date

bp = Blueprint('admin', __name__)

# grant access for admin to specific secure routes
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.role != "admin":
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)

    return decorated_function

@bp.route("/admin/products", methods=["GET"])
@admin_required
def admin_products():
    stmt = db.select(Product).order_by(Product.name)
    products = db.session.execute(stmt).scalars().all()
    return render_template("admin/products_list.html", products=products)


@bp.route("/admin/products/<int:id>/edit", methods=["GET", "POST"])
@admin_required
def admin_edit_product(id):
    return render_template("products.html")

@bp.route("/admin/products/<int:id>/delete", methods=["POST"])
@admin_required
def admin_del_product(id):
    render_template("products.html")

@bp.route("/admin/products/add", methods=["POST", "GET"])
@admin_required
def admin_add_product():
    print("Admin Add Product")
    form = AddProduct()

    if request.method == "POST":
        if not form.validate():
            flash('There was a problem with your submission')
            return render_template('admin/add_product.html', form=form)
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
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash('There was a problem with your submission')
                return render_template('admin/add_product.html', form=form)

            flash(f'Successfully added a new product: {form.name.data}')
            return redirect(url_for("admin.admin_products"))

    recent = db.session.execute(db.select(Product).order_by(Product.name)).scalars().all()
    # db.session.close() # close the session after the operation

    return render_template("admin/add_product.html", recent=recent, form=form)
