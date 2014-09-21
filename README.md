# django-exceptions

package enable any project to redirect a user to a view when an exception is raised

## installation

pip install django-exceptions

add 'djexceptions' to your INSTALLED\_APPS
and 'djexceptions.middleware.ExceptionsMiddleware' to your middleware

## use case

``` python
if …:
    raise ApiLatencyException
…

class ApiLatencyException(RedirectException):
    view_name = 'home'
```

When the exception will be raised, this will redirect the user to the
'home' page.
