"""bfs_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from apps.general.views import *
from apps.feedback.views import *


handler404 = 'apps.general.views.page_not_found_view'
handler500 = 'apps.general.views.internal_server_error_view'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.feedback.urls')),
    url(r'^', include('apps.general.urls')),
    url(r'^$', HomeView.as_view()),
    url(
        r'^devbot/',
        include('apps.django_chatterbot.urls',
        namespace='chatterbot')
    ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
