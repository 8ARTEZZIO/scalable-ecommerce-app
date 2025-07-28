# 🛒 Scalable E-Commerce System

A scalable e-commerce backend built with **Flask**, **PostgreSQL**, **SQLAlchemy**, and **Bootstrap** for clean and responsive UI display. This project is designed with extensibility, modularity, and real-world architecture in mind.

---

## Features

- ✅ User registration and login
- ✅ Product catalog (CRUD for admin)
- ✅ Shopping cart system
- ✅ Checkout and order history
- ✅ Admin-only controls for product management
- ✅ Bootstrap-based responsive UI
- ✅ Clean project structure for scalability

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
ecommerce/
├── app/
│ ├── models/
│ ├── routes/
│ ├── templates/
│ ├── static/
│ └── utils/
├── migrations/
├── config.py
├── run.py
└── requirements.txt
```

---

## Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/scalable-ecommerce-app.git
cd scalable-ecommerce-app
```
2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependecies**
```bash
pip install -r requirements.txt
```
4. **Set up the database**
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
5. **Run the app**
```bash
flask run
```

---

## 🙌 Contributions

Pull requests and contributions are welcome. Please open an issue first to discuss what you would like to change or add.

---

## 📄 License

This project is licensed under the MIT License.

---

## Author

Bartlomiej Kuzma
Inspired to bring clarity, structure, and real-world architecture into every line of code.
