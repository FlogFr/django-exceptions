from django.core.urlresolvers import reverse
from django.http import (
    HttpResponseRedirect,
    Http404,
)
from .exceptions import RedirectException


class ExceptionsMiddleware(object):
    """
    Middleware to process custom exception and redirect
    the user to the view
    """
    def process_exception(self, request, exception):
        print(u'processing exception')
        if isinstance(exception, RedirectException):
            print(u'we have a good one')
            view_name = exception.view_name
            try:
                view = reverse(view_name)
                return HttpResponseRedirect(view)
            except:
                raise Http404
