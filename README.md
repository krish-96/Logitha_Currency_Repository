# Logitha_Currency_Repository
This project is created to play with Django Functionalities.


--> For adding Django Password Reset Views

settings.py
````````````````````````````````````
INSTALLED_APPS = [

    ...
    'django.contrib.auth',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
````````````````````````````````````

urls.py:
````````````````````````````````````
from django.contrib.auth import views as auth_views

urlpatterns = [
    ...
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
````````````````````````````````````
Or you can simply include all auth views:
````````````````````````````````````
urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
]
````````````````````````````````````

List of required templates:
````````````````````````````````````
registration/password_reset_form.html
registration/password_reset_subject.txt
registration/password_reset_email.html
registration/password_reset_done.html
registration/password_reset_confirm.html
registration/password_reset_complete.html

````````````````````````````````````

