from django.conf.urls import url

from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.views import login, logout

from . import forms
from . import views

urlpatterns = [
    url(r'^main/', views.MainView.as_view()),
    url(r'^login/', login, {'template_name': 'login.html','authentication_form': forms.LoginForm}, name='login'),
    url(r'^logout/$', logout, {'next_page': '/exit'}, name='logout'),
    url(r'^new/', TemplateView.as_view(template_name='feedback/new_form.html')),
    url(r'^exit/', views.exit_view),
    url(r'^done_cron/(?P<dept_name>[\w\-]+)$',views.done_cron),
    url(r'^done', views.done_view),
    url(r'^faculty-pending/', views.faculty_remaining),
    url(r'^dashboard/', views.Dashboard, name='dashboard'),
    url(r'^notify/', views.notifyView, name='notify'),
    url(r'^completed/', views.counter_view, name='counter_view'),
    url(r'^send_message/', views.send_text_message_view, name='send_text_message_view'),
    url(r'^progress/', views.show_message_sent_view, name='show_message_sent_view'),
    url(r'^ping-report/$',views.ping_url, name='ping_url'),

    #url(r'^consolidated/', views.consolidated.as_view(), name='feedback/consolidated_report'),
]
