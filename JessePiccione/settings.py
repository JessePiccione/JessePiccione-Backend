import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY_VAR')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DBENGINE=os.getenv('DATABASE_ENGINE')
DBNAME=os.getenv('DATABASE_NAME')
DBHOST=os.getenv('DATABASE_HOST')
DBPORT=os.getenv('DATABASE_PORT')
DBUSER=os.getenv('DATABASE_USERNAME')
DBPASSWORD=os.getenv('DATABASE_PASSWORD')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'Authorization',
    'Content-Type',
    'origin',
    'x-csrftoken',
]
CORS_ALLOW_CREDENTIALS=False
CORS_ALLOWED_ORIGINS = [
                        'http://localhost:3000',
                        'https://www.jessepiccione.info',
                        'https://jessepiccione.info', 
                        'https://piccione.dev',
                        'https://portal.piccione.dev'
                        ]
CSRF_TRUSTED_ORIGINS = [
                        'http://localhost:3000',
                        'https://www.jessepiccione.info',
                        'https://jessepiccione.info', 
                        'https://piccione.dev',
                        'https://portal.piccione.dev'
                        ]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# HTTPS MODE
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False 
CSRF_COOKIE_SECURE = True
# Application definition
INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'JessePiccioneAssistant.apps.JessepiccioneassistantConfig',
    'Message.apps.MessageConfig',
    'Awards.apps.AwardsConfig',
    'Projects.apps.ProjectsConfig',
    'Skills.apps.SkillsConfig',
    'Education.apps.EducationConfig',
    'WorkExperience.apps.WorkexperienceConfig',
    'Resume.apps.ResumeConfig',
    'ResumeAPI.apps.ResumeapiConfig',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
ROOT_URLCONF = 'JessePiccione.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'JessePiccione.wsgi.application'
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': DBENGINE,
        'NAME': DBNAME,
        'HOST': DBHOST,
        'PORT': DBPORT, 
        'USER': DBUSER,
        'PASSWORD': DBPASSWORD,
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = 'static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES":[
        'rest_framework.authentication.TokenAuthentication',  
    ]
}
CACHES = {
    "default":{
        "BACKEND":"django.core.cache.backends.db.DatabaseCache",
        "LOCATION":"backend_mysql_cache",
    }
}
