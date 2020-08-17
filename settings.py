import os
import sys
from create_database import psycopg2
from encryption import hash_me

sys.path.append(os.path.abspath('./libs'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG


ADMINS = (
    ('Andrew Roe', 'aroe3sec@gmail.com')
)

#sets database connection from database file 
DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'passwordsafedb',
        'USER': 'aroe',
        'PASSWORD': 'Coldwell980869#',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

