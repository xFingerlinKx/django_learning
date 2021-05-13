"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+ucpuj-nk8v0h9_z8+8jrs^%jk2z9af329jctcllposs#d+lr#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # административный веб-сайт Django
    'django.contrib.auth',  # реализует подсистему разграничения доступа
    'django.contrib.contenttypes',  # хранит список всех моделей, объявленных во всех приложениях сайта.
                                    # Необходимо при создании полиморфных связей между моделями
    'django.contrib.sessions',  # реализует подсистему, обслуживающую серверные сессии
    'django.contrib.messages',  # выводит всплывающие сообщения
    'django.contrib.staticfiles',  # обрабатывает статические файлы
    # подключаемые приложения
    'bboard.apps.BboardConfig',

]
# Посредник (middleware) Django — это программный модуль, выполняющий предварительную
# обработку клиентского запроса перед передачей его контроллеру и окончательную обработку ответа,
# сгенерированного контроллером, перед его отправкой клиенту.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # реализует дополнительную защиту сайта от сетевых атак
    'django.contrib.sessions.middleware.SessionMiddleware',  # обрабатывает серверные сессии на низком уровне
    'django.middleware.common.CommonMiddleware',  # участвует в предварительной обработке запросов
    'django.middleware.csrf.CsrfViewMiddleware',  # осуществляет защиту ОТ межсайтовых атак при обработке данных,
                                                  # переданных сайту HTTP-методом POST
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # добавляет в объект запроса атрибут, хранящий текущего
    # пользователя. Через этот атрибут в контроллерах и шаблонах можно выяснить, какой пользователь
    # выполнил вход на сайт и выполнил ли вообще
    'django.contrib.messages.middleware.MessageMiddleware',  # обрабатывает всплывающие сообщения на низком уровне
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # реализует дополнительную защиту сайта от сетевых атак
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        # путь к модулю шаблонизатора, записанный в виде строки
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # список путей к папкам, в которых шаблонизатор будет искать шаблоны (по умолчанию — пустой список)
        'DIRS': [],
        # если True, то шаблонизатор дополнительно будет искать шаблоны в папках templates, располагающихся
        # в пакетах приложений. Если False, то шаблонизатор станет искать шаблоны исключительно в папках из списка dirs
        # . Значение по умолчанию — False, однако во вновь созданном проекте устанавливается В True
        'APP_DIRS': True,
        # дополнительные параметры, поддерживаемые конкретным шаблонизатором. Также указываются
        # в виде словаря, элементы которого задают отдельные параметры
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

WSGI_APPLICATION = 'samplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE — код языки, на котором будут выводиться системные сообщения
# и страницы административного сайта, в виде строки
LANGUAGE_CODE = 'ru'
# TIME_ZONE - обозначение временной зоны в виде строки. По умолчанию — "America/Chicago".
# Однако сразу же при создании проекта ему присваивается значение "UTC" (всемирное координированное время)
TIME_ZONE = 'UTC'
# USE_I18N — если True, будет активизирована встроенная в Django система автоматического перевода на язык,
# записанный в параметре LANGUAGE_CODE, после чего все системные сообщения и страницы административного
# сайта будут выводиться на этом языке. Если False, автоматический перевод выполняться не
# будет, и сообщения и страницы станут выводиться на английском языке
USE_I18N = True
# USE_L10N - если True, числа, значения даты и времени при выводе будут форматироваться по правилам языка из параметра
# LANGUAGE_CODE. Если False, все эти значения будут форматироваться согласно настройкам, заданным в проекте
USE_L10N = True
# если True, Django будет хранить значения даты и времени с указанием временной зоны, в этом случае параметр
# TIME_ZONE указывает временную зону по умолчанию. Если False, значения даты и времени будут храниться без
# отметки временной зоны, и временную зону для них укажет параметр TIME_ZONE
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'bboard/static')
]
# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'accounts/login/'
