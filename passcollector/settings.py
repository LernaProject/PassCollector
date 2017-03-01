import os.path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "xlsf5^ajgyf+a2nwzz7pbd$pemguotb967rh&@31nls0l6_qra"

DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]", "172.16.0.90"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "main",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

ROOT_URLCONF = "passcollector.urls"

LOGGING = { "version": 1 }
