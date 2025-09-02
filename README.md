# Scalable E-Commerce System [in progress...]

A scalable e-commerce backend built with **Flask**, **PostgreSQL**, **SQLAlchemy**, and **Bootstrap** for clean and responsive UI display. This project is designed with extensibility, modularity, and real-world architecture in mind.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ca19ce9b-ad7a-4aac-8774-c81da7a081a7" />

---

## Features ( ✅ if done )

- [ ] User registration and login (can create account, log in/out, and @login_required pages work):
  - [x] Model: `Users` with `id, username, email(unique), password_hash, role(default="user")`
  - [ ] Flask-Login glue: `user_loader, login_view, @login_required`
  - [ ] Forms: `RegisterForm, LoginForm` (Flask-WTF; email validator)
  - [ ] Routes: `/register` (GET/POST), `/login` (GET/POST), `/logout` (POST/GET)
  - [ ] Templates: `register.html, login.html`; navbar shows Login/Logout state
  - [ ] Flash messages + redirects (POST→Redirect→GET)
- [ ] Product catalog (browse/search/detail works with seed data):
  - [ ] Product list: `/products` with pagination, basic search `?q=`, sort by price/date
  - [ ] Product detail: `/products/<slug_or_id>` with image, price, description
  - [ ] Templates: `products.html` (grid), `product.html` (detail)
  - [ ] Optional: API endpoints `/api/products` for future JS
- [ ] Admin-only product management (CRUD) (admin can create/edit/disable products; non-admins 403):
  - [ ] Authorization: `@admin_required` decorator (checks `current_user.role == "admin"`)
  - [ ] Admin blueprint: `/admin`
  - [ ] Routes: list, create, edit, delete:
    - [ ] `GET /admin/products`
    - [ ] `GET/POST /admin/products/new`
    - [ ] `GET/POST /admin/products/<id>/edit`
    - [ ] `POST /admin/products/<id>/delete`
  - [ ] Forms: `ProductForm` (name, slug, price, stock, is_active, image URL)
  - [ ] Templates: `admin/products_list.html, admin/product_form.html`
- [ ] Shopping cart system (add/update/remove works; totals update; empty cart path handled):
  - [ ] Models:
    - [ ] `Cart: id, user_id(unique), created_at, updated_at`
  - [ ] `Services: add_to_cart(product, qty), update_qty(item, qty), remove_item(item), cart_total(cart)`
  - [ ] Routes:
    - [ ] `POST /cart/add` (from product detail/list)
    - [ ] `GET /cart` (view)
    - [ ] `POST /cart/update/<item_id>` (change qty)
    - [ ] `POST /cart/remove/<item_id>`
  - [ ] Template: `cart.html` (line items, qty inputs, totals)
  - [ ] Stock guard: prevent qty > stock; show message
- [ ] Checkout and order history (you can place an order, see confirmation, and view past orders):
  - [ ] Models:
    - [ ] `Orders: id, user_id(nullable for guest), status(pending/paid), subtotal, tax_total, shipping_total, grand_total, currency, placed_at, shipping_name/line1/city/postcode/country`
    - [ ] `OrderItem: id, order_id, product_id, product_name, unit_price, quantity, line_total`
  - [ ] FLow:
    - [ ] `GET /checkout`: show shipping form + order summary
    - [ ] `POST /checkout`: validate stock, create `Order` + `OrderItems` (snapshot name/price), decrement stock, clear cart, redirect to `/orders/<id>/confirmation`
  - [ ] Order history:
    - [ ] GET /account/orders (list user’s orders)
    - [ ] GET /orders/<id> (detail; 404 if not owner unless admin)
  - [ ] Templates: `checkout.html, order_confirmation.html, orders.html, order_detail.html`   
- [ ] Admin-only controls for product management (basic ops: admin can view and change order status):
  - [ ] Admin list: `GET /admin/orders` with filters by status/date
  - [ ] Admin detail: `GET /admin/orders/<id>` showing items and addresses
  - [ ] Status transitions: `POST /admin/orders/<id>/status` (pending → paid → fulfilled → cancelled)
- [ ] Bootstrap-based responsive UI (pages look consistent on mobile/desktop):
  - [x] `base.html`: navbar (brand + search), footer, flash partial
  - [ ] Make forms pretty: use `form-floating`, validation messages
  - [ ] 404/500 page
  - [ ] Sticky header + centered hero search on `/`
  - [x] Dark Theme + small custom CSS (loaded after Bootstrap)
  - [ ] Accessibility pass: labels, aria, focus states
- [ ] Clean project structure for scalability (new contributors can run the app in minutes):
  - [x] Project structure: app factory, blueprints, `extensions.py, config.py, wsgi.py`
  - [x] README.md: quick start (SQLite + Docker Postgres), .env.example
  - [ ] Gunicorn command documented; Dockerfile/compose later if you want 

---

## Tech Stack

| Layer        | Tech                          |
|--------------|-------------------------------|
| Backend      | Flask, Flask-SQLAlchemy       |
| Database     | PostgreSQL                    |
| Frontend     | Bootstrap 5, Jinja2 Templates |
| Auth         | Flask-Login                   |
| Forms        | Flask-WTF                     |
| Migrations   | Flask-Migrate                 |

---

## Project Structure

```
scalable-ecommerce-app/
├── app/
│ ├── static/
│ │ └── styles.css
│ ├── templates/
│ │ ├── 404.html
│ │ ├── base.html
│ │ ├── cart.html
│ │ ├── checkout.html
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── product.html
│ │ └── products.html
│ ├── __init__.py
│ ├── api.py
│ ├── config.py
│ ├── extensions.py
│ └── models.py
├── alembic.ini
├── wsgi.py
├── Procfile
├── config.py
├── run.py
└── requirements.txt
```
---

## Prerequisites
- Python **3.12** (check with `python --version`)
- (Optional) Docker Desktop for Postgres, or a local PostgreSQL 16+

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/scalable-ecommerce-app.git
cd scalable-ecommerce-app
```
2. **Virtual env (Python 3.12)**
```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```
3. **Install dependecies**
```bash
pip install -r requirements.txt
```
4. **Environment**
```bash
cp .env.example .env
```
  By default we use SQLite:

```env
# pick ONE of these:

# (Default) SQLite — no install needed
DATABASE_URL=sqlite:///dev.db

# PostgreSQL (Docker or native)
# DATABASE_URL=postgresql+psycopg://ecom_user:ecom_pass@127.0.0.1:5432/ecom

APP_ENV=dev
SECRET_KEY=change-me
```
5. **Set up the database**
- If migrations already exist (repo has migrations/):
```bash
flask --app run.py db upgrade
```
- If this is the first time creating migrations:
```bash
flask --app run.py db init
flask --app run.py db migrate -m "initial schema"
flask --app run.py db upgrade
```
6. **Run the app**
```bash
flask --app run.py run
```

---

## Contributions

Pull requests and contributions are welcome. Please open an issue first to discuss what you would like to change or add.

---

## License

This project is licensed under the MIT License.

---

## Author

Bartlomiej Kuzma
