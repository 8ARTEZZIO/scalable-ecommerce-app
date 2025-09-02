"""
All the SQLAlchemy models.
[data shapes + relationships]
Keep it framework-agnostic and light.
"""
from datetime import datetime
from .extensions import db, Base
from sqlalchemy import String, DateTime, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin


user_orders = db.Table(
    "user_orders",
    db.Column("cart_id", db.ForeignKey("cart_table.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("products_table.id"), primary_key=True),
)

order_product = db.Table(
    "order_product",
    db.Column("order_id", db.ForeignKey("order_table.id"), primary_key=True),
    db.Column("product_id", db.ForeignKey("products_table.id"), primary_key=True),
)


class Users(UserMixin, db.Model):
    __tablename__ = "users_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column(String(225))
    role: Mapped[str] = mapped_column(default="user")
    created_at: Mapped[str] = mapped_column(DateTime)
    carts: Mapped["Cart"] = relationship(back_populates="users")
    orders: Mapped[list["Order"]] = relationship(back_populates="users")


class Products(db.Model):
    __tablename__ = "products_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(225))
    slug: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]
    currency: Mapped[str]
    description: Mapped[str] = mapped_column(String(500))
    main_image_url: Mapped[str]
    stock: Mapped[int]
    is_active: Mapped[bool]
    created_at: Mapped[str] = mapped_column(DateTime)
    updated_at: Mapped[str]
    order: Mapped[list["Order"]] = relationship(
        secondary=order_product,
        back_populates="products"
    )
    # (Optional, later) product_images: (id, product_id, url, alt_text, position)
    # (Optional, later) categories + product_categories (many-to-many)


class Cart(db.Model):
    __tablename__ = "cart_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[str] = mapped_column(DateTime)
    updated_at: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    users: Mapped["Users"] = relationship(back_populates="cart")
    children: Mapped[list[Products]] = relationship(secondary=user_orders)


class Order(db.Model):  # finalized purchase
    __tablename__ = "order_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"), nullable=True)
    users: Mapped["Users"] = relationship(back_populates="order")
    products: Mapped[list[Products]] = relationship(
        secondary=order_product,
        back_populates="order"
    )
    status: Mapped[str]
    subtotal: Mapped[int]
    tax_total: Mapped[int]
    shipping_total: Mapped[int]
    discount_total: Mapped[int]
    grand_total: Mapped[int]
    currency: Mapped[str]
    placed_at: Mapped[datetime | None] = mapped_column(db.DateTime)
    billing_address_id: Mapped[str]
    shipping_address_id: Mapped[str]

    # order_items (association with price snapshot):
    # id, order_id, product_id, product_name, sku (optional),
    # unit_price, quantity, line_total
    #
    # (Store product_name/unit_price here to freeze what was bought at that time.)


class Addresses(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(nullable=True)
    full_name: Mapped[str]
    line1: Mapped[str]
    line2: Mapped[str]
    city: Mapped[str]
    region: Mapped[str]
    postal_code: Mapped[str]
    country: Mapped[str]
    phone: Mapped[int] = mapped_column(unique=True)


class Payments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(nullable=True)
    provider: Mapped[str]
    provider_ref: Mapped[str]
    amount: Mapped[int]
    currency: Mapped[str]
    status: Mapped[str]
    captured_at: Mapped[str]


class Shipments(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(nullable=True)
    carrier: Mapped[str]
    service: Mapped[str]
    tracking_number: Mapped[str]
    status: Mapped[str]
    shipped_at: Mapped[str]
    delivered_at: Mapped[str]

    # (Optional later: reviews, coupons/promotions, wishlists, inventory by location, product_variants for size/color)


#TODO
# Connect all the relationships
# Relationships (at a glance) put '✔' if done
# [✔]User 1—1 Cart: users.id → carts.user_id (unique)
# [✔]Cart — Product: cart_items (cart_id, product_id, quantity)
# [✔]User 1— Orders*: orders.user_id (nullable for guests)
# [ ]Order — Product: order_items (order_id, product_id, quantity, unit_price, …)
# [ ]Order 1—1 Address (billing/shipping): FK(s) to addresses or inline address fields on orders
# [ ]Order 1— Payments*, Order 1— Shipments*