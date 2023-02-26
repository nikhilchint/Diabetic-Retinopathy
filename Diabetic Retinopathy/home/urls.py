from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
# from . import views
urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("service",views.service,name='service'),
    path("contact",views.contact,name='contact'),
    path("detect",views.detect,name='detect'),
    path("result",views.result,name='result'),
    path("report",views.report,name="report"),
    # path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),

    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
