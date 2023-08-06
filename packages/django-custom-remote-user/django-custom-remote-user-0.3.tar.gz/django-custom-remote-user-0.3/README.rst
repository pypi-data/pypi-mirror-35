=====
Custom Remote User
=====

Custom Remote User is a Django app that extends remote user authentication
enabling custom common behavior. The app currently offers only a case-insensitive
backend `CaseInsensitiveRemoteUserBackend`.

`CaseInsensitiveRemoteUserBackend` guarantees that all users created using an 
external authentication service are created with an all-lower case username.
This is important because some external authentication services return a 
case-sensitive username upon login. This is problematic with Django as the built-in
user model is case-sensitive. This means a single remote user may have two different
records in that database (e.g. 'Username' is different than 'username').


Quick start
-----------

1. Add "custom_remote_user" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'custom_remote_user',
    ]

2. Add CaseInsensitiveRemoteUserBackend::

    AUTHENTICATION_BACKENDS = [
        'custom_remote_user.backends.CaseInsensitiveRemoteUserBackend',
    ]

3. Add the required middlewares for remote user authentication::

    MIDDLEWARE = [
        ...
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.RemoteUserMiddleware',
        ...
    ]
