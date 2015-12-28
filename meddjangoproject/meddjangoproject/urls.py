"""meddjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

# This means that medron.org/core will take them to the_big_one
# medron.org/admin will take us to the admin site
# I did this so that medron.org can be the ladning page, but they have to go
# to core to get into the core functionality. The actual core page will be
# blank similar to theonion.com's /section/ page

# TODO re-think this so that people can access doctors from .../doctors/2
# instead of .../core/doctors/2
urlpatterns = [
    url(r'^core/', include('the_big_one.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homepage.views.index'),
]
