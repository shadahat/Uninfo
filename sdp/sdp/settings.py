import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = BASE_DIR


####################################################################
#                     Social Media Login                           #
####################################################################
# Author : Noboni & Shahin #


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'


SOCIAL_AUTH_GITHUB_KEY = '31ecd19bf8f1533ac527'
SOCIAL_AUTH_GITHUB_SECRET = '48bb63faeba769d43da8b5834fff949dc61a6cdb'


SOCIAL_AUTH_TWITTER_KEY = 'eJffGMtO9XLojnW97LYpnYvvH'
SOCIAL_AUTH_TWITTER_SECRET = 'LKDlzUkMq1qQpo2dgHN21l4v9vcNAcUL9NijfuAdHFiRXW2UfJ'


SOCIAL_AUTH_LINKEDIN_KEY = '8158am3wo745vd'
SOCIAL_AUTH_LINKEDIN_SECRET = 'DP51ZcNwvSfv26Bx'



MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
STATIC_URL = '/static/'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*%7a1+vk*kip!-ko!+nqrw#_^=am(o&+jku27g2(6hu873t&5j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'Login',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'sdp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth',

    'django.contrib.auth.backends.ModelBackend',
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    os.path.join(SITE_ROOT, 'staticfiles'),
)

WSGI_APPLICATION = 'sdp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'UniDB',
        'USER': 'root',
        'PASSWORD': 'qwe123',
        'HOST': 'localhost',
        'PORT': '',

    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

####################################################################
#                     Social Media Login                           #
####################################################################


SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress' , ]

SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'id',
    'first-name',
    'last-name',
    'location',
    'public-profile-url',
    'headline',
    'industry',
    'summary',
    'positions',
]

SOCIAL_AUTH_LINKEDIN_EXTRA_DATA = [
    ('id', 'id'),('summary','summary'), ('positions','positions') , ('headline', 'headline'),('industry','industry'),
    ('public-profile-url', 'public_profile_url'),
    ('location', 'location'),
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

