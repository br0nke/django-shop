# django-shop
## Django Web Shop

This is a Django-based web shop project featuring user profiles, listings with photos, and category organization.

**Features:**

* User registration and login
* User profiles with customizable information
* Product listings with descriptions, photos, and categories(can be changed/added more in model.py) search function
* More will be added soon(cart, user to user messages, shipping calculator)!

**Getting Started:**

1. **Clone the repository:**

```bash
git clone https://github.com/br0nke/django-shop.git
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up the database:**

* Create a database according to your preference (e.g., MySQL, PostgreSQL).
* Update the `DATABASES` settings in `settings.py` with your database credentials.

4. **Run migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser:**

* Open a terminal in your project directory.
* Run the following command, providing your desired username, email, and password twice:

```bash
python manage.py createsuperuser
```

6. **Start the development server:**

```bash
python manage.py runserver
```

**Usage:**

1. **Visit `http://localhost:8000/` in your browser.**
2. **Register or login as a user.**
3. **Navigate to the relevant sections to manage your profile, create or browse listings, and explore categories (depending on your implementation).**

**License:**

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3. See the `LICENSE` file for details.
