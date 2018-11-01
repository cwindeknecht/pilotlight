from django.urls import path

from . import views

app_name = 'pilot'
urlpatterns = [
    path('', views.index, name='index'),
    path('calendar', views.calendar, name='calendar'),
    path('show/<int:show_id>', views.show, name="show"),
]
