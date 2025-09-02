# Scalable E-Commerce System [in progress...]

A scalable e-commerce backend built with **Flask**, **PostgreSQL**, **SQLAlchemy**, and **Bootstrap** for clean and responsive UI display. This project is designed with extensibility, modularity, and real-world architecture in mind.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ca19ce9b-ad7a-4aac-8774-c81da7a081a7" />

---

## Features ( ✅ if done )

- [ ] User registration and login
- [ ] Product catalog (CRUD for admin)
- [ ] Shopping cart system
- [ ] Checkout and order history
- [ ] Admin-only controls for product management
- [ ] Bootstrap-based responsive UI
- [ ] Clean project structure for scalability

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
