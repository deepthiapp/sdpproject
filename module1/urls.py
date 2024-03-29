from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travel/', travelpackage, name='travelpackage'),
    path('print_to_console/',print_to_console,name='print_to_console'),
    path('print1/',print1,name='print1'),
    path('ran1/', ran, name='ran'),
    path('ran/', random123, name='random123'),
    path("date1/",getdate1,name="getdate1"),
    path("date/",get_date,name="get_date"),
    path('tzfunctional',tzfunctional,name="tzfunctional"),
    path('db/',dataconnection,name='dataconnection'),
    path('dbc/',registerloginfunction,name='registerloginfunction'),
    path('chart/',pie_chart,name='pie_chart'),
    path('images/',images,name='images'),
    path('td/',timedisplay,name='timedisplay'),
    path('wh/',weatherlogic,name='weatherlogic'),
    path('login/',login,name='login'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('login1/', login1, name='login1'),
    path('logout/',logout,name='logout'),
    path('fb/',fback,name='fback'),
    path('cm/',contactmail,name='contactmail'),

]
