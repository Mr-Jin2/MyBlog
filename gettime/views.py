# Create your views here.
#coding=utf8
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import *
from django.http import Http404, HttpResponse
import datetime

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('gettime/current_datetime.html', {'current_date': current_date})

def HoursAhead(request,offset):
    try:
        offset=int(offset)
        print offset
    except ValueError:
        raise Http404
    now = datetime.datetime.now()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>It is now %s, after %d hours is %s </body></html>" % (now,offset,dt)

    # t=get_template('current_datetime.html')
    # html=t.render(Context({'current_date':now}))
    # return HttpResponse(html)

    return render_to_response('gettime/hours_ahead.html', {'next_time': dt, 'hour_offset':offset})

def ua_display_good1(request):
    try:
        ua = request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("Your browser is %s" % ua)

