## Getting Started

1. Fork / clone the project.
2. Create an environment file .env file with your projects secret keys
  - DB_HOST = localhost
  - DB_USER = ''  
  - DB_PASS = ''
  - DB_NAME = ''
  - DB_PORT = 5432 
  - DB_PASSWORD = ' '
  - DB_USER = ' '
  - ADMIN_ROOT = ' '
  - ADMIN_PW = ' '
  - ADMIN_DB = ' '
  - MAP_BOX_KEY = ' '
  - SQLALCHEMY_DATABASE_URI = ' '
  - SQLALCHEMY_BINDS = ' '
  - SECRET_KEY = ' '
  - WTF_CSRF_SECRET_KEY = ' '
  - HCAPTCHA_SITE_KEY = ' '
  - HCAPTCHA_SECRET_KEY = ' '
  - CONTACT_MAIL = ' '
  - FLASK_DEBUG = ' '
  - FLASK_ENV = ' '
  - JOB_IMAGES = ' '
  - UPLOAD_FOLDER = ' '
  - BLOG_IMAGES = ' '
  - CLIENT_IMAGES = ' '
3. Install venv - `sudo apt install python3-venv`
4. Choose some directory and run this command `python3 -m venv venv`
5. Activate the venv `source venv/bin/activate`
6. Install dependencies: `pip3 install -r requirements.txt`
7. Visit `http://localhost:5000/`