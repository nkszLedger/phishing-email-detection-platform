
# PHISHING EMAIL DETECTION ENHANCEMENT: MITIGATING PHISHING THREATS USING AI

Email communication continues to become a critical essential tool for businesses and the public in modern society. As a result, cyber attackers have made email services the prime method for conducting malicious cyber attempts. Although email infrastructure has evolved, phishing attempts continue to present significant risks such as financial fraud, credential harvesting amongst other risks on end-users. 

The aim of the project seeks to develop a deep learning (DL) based phishing detection model that will be integrated into this presentational web user interface demonstrating an experimental phishing email detection. The project shall focus on email content written in the English language to train and test DL models utilizing natural language processing (NLP) techniques. This guides provides developers with setting up the development environment for the web user interface.


# Development Environment Setup

How to setup the project using `virtualenv` on Ubuntu Operating System (OS).

---

## **1. Install Python and Virtualenv**
Ensure that Python is installed on OS (preferably Python 3.8+).

```sh
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

Install `virtualenv`:

```sh
pip3 install virtualenv
```

---

## **2. Create or Activate the Virtual Environment**
Navigate to the project directory and create a virtual environment:

```sh
cd ~/phishingdetectionplatform
virtualenv venv
```

Activate the virtual environment:

```sh
source venv/bin/activate
```

The terminal should show `(venv)` at the beginning of the line which indicates that the virtual environment is now active.

---

## **3. Install Django and Required Dependencies**
Install Django and other dependencies (Ensure the `(venv)` is active):

Navigate to the folder where `requirements.txt` exists

```sh
cd ~/phishingdetectionplatform
```

```sh
pip install -r requirements.txt
```

To verify the Django installation:

```sh
python -m django --version
```

---

## **4. Setup PostgreSQL database**
Follow the instructions here:

## Links
[Install and Configure PostgreSQL and pgAdmin on Ubuntu 20.04 | 22.04](https://medium.com/yavar/install-and-configure-postgresql-and-pgadmin-on-ubuntu-20-04-22-04-52c52c249b9e)
---

## **5. Configure Environment Variables**
Set up a `.env` file for storing sensitive information:

```sh
touch .env
```

Edit the file to include necessary configurations:

```
SECRET_KEY=your_secret_key
DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=your_db_name
SQL_USER=your_db_user
SQL_PASSWORD=your_db_password
SQL_HOST=localhost
SQL_PORT=5432
```

Load environment variables in `settings.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG") == "True"
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS").split(",")

...
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE'),
        'NAME': os.environ.get('SQL_DATABASE'), 
        'USER': os.environ.get('SQL_USER'),
        'PASSWORD': os.environ.get('SQL_PASSWORD'),
        'HOST': os.environ.get('SQL_HOST'), 
        'PORT': os.environ.get('SQL_PORT'),
    }
}
```

---

## **6. Run Migrations and Start Server**
Apply migrations:

```sh
python manage.py migrate
```

Create a superuser (optional):

```sh
python manage.py createsuperuser
```
---

## **7. Seed the database**
Upload the `db_seed` dataset from modelling directory to database
---
## **8. Start Server**
Start the development server:

```sh
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---
## **9. Running Predictions** 
Ensure that models have been deployed (Step 5 of the modelling README.md). Open `apps.py` file in `phishingdetectionplatform/phishdetector` directory and uncomment the `ready()` function:
```python
from django.apps import AppConfig
import threading
import time

class PhishdetectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phishdetector'

    # def ready(self):
    #     """ Start the background thread when Django starts """
    #     from phishdetector.tasks import start_prediction_thread
        
    #     prediction_start_time = time.time()
    #     if threading.main_thread().is_alive():  # Prevent multiple threads
    #         start_prediction_thread()
    #     prediction_end_time = time.time()
    #     duration = round(prediction_end_time - prediction_start_time, 4)
    #     print("PhishdetectorConfig.ready(): Background prediction thread complete.")
    #     print(f"PhishdetectorConfig.ready(): Prediction thread took [{duration}] seconds to complete.")
```
---

## **10. Deactivating the Virtual Environment**
When you're done, deactivate the virtual environment:

```sh
deactivate
```

To reactivate later:

```sh
source venv/bin/activate
```

---

## **11. Helper Commands**
### **Installing a New Package**
```sh
pip install package_name
```

### **Saving Installed Packages**
After installing new packages, update `requirements.txt`:

```sh
pip freeze > requirements.txt
```

### **Removing the Virtual Environment**
To delete the virtual environment:

```sh
rm -rf venv
```

---

