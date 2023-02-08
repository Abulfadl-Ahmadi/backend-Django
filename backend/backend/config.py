import os
from pathlib import Path


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REAL_BASE_DIR = Path(__file__).resolve().parent.parent.parent

postgresql = {
    'Abulfadl': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NewDB1',
        'USER': 'postgres',
        'PASSWORD': 'Abul1385',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },

    'Farsi': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NewDB',
        'USER': 'postgres',
        'PASSWORD': '12457800@MHf',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },
    
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

