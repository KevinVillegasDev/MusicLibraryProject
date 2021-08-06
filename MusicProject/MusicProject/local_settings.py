SECRET_KEY = 'django-insecure-y0m*24hhacnh!u055ci28@$r8kravvyt-+fyy%q63*rvrx0n7%'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}