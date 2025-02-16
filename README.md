# e_comprj

## Overview
**e_comprj** is an e-commerce web application built using Django. This project is currently in development and includes user authentication, an admin panel, and basic core functionality.

## Features
- User registration and authentication
- Admin panel using Jazzmin
- Custom user model with email authentication
- Static and media file handling
- Modular app structure (`core`, `userauths`)

## Tech Stack
- **Backend:** Django 5.1.5
- **Database:** SQLite (default, can be switched to PostgreSQL or MySQL)
- **Admin Panel:** Jazzmin
- **Frontend:** Django Templates, HTML, CSS (to be expanded)

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/e_comprj.git
cd e_comprj
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Development Server
```bash
python manage.py runserver
```
Access the app at **`http://127.0.0.1:8000/`**

## Project Structure
```
e_comprj/
│── core/              # Main application logic
│── userauths/         # User authentication system
│── templates/         # HTML templates
│── static/            # Static files (CSS, JS, images)
│── media/             # User-uploaded media files
│── e_comprj/          # Project settings and configuration
│── db.sqlite3         # SQLite database (changeable)
│── manage.py          # Django management script
```

## Troubleshooting
### 1. URL Not Found (404 Errors)
- Ensure `userauths/urls.py` and `core/urls.py` exist and are properly included in `e_comprj/urls.py`.
- Check registered URLs using:
  ```bash
  python manage.py show_urls
  ```

### 2. Database Issues
If migrations are not working properly, reset them:
```bash
rm -rf userauths/migrations core/migrations
python manage.py makemigrations
python manage.py migrate
```

### 3. Debugging Views
To confirm that a view is being accessed, add a debug print inside the function:
```python
print("✅ View is being called")
```
Then restart the server and check the console output.

## Next Steps
- Implement product listings
- Add cart and checkout functionality
- Improve frontend UI with Bootstrap or Tailwind CSS
- Deploy to production (AWS, Heroku, or DigitalOcean)

## Contributors
- Junior Johnson - Developer

## License
This project is licensed under the MIT License.

