Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from django.urls import path
    from . import views
    urlpatterns = [
    path('', views.post_list, name='post_list'),
]
