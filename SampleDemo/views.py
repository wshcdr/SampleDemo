__author__ = 'python'

from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

#
#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><head></head><body>datetime now:%s</body></html>" % now
#    return HttpResponse(html)
#

def hours_ahead(request, offset):
    """

    :param request:
    :param offset:
    :return:
    """
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hours is will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template("current_datetime.html")
    #t = Template('<html><body>现在时刻是:{{current_datetime}}</body></html>')
    c = Context({'current_datetime': now})
    html = t.render(c)
    return HttpResponse(html)


