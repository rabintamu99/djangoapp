from django.contrib import admin
from django.urls import path
from home import views
from .views import SignUpView


urlpatterns = [
    path('', views.index, name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),

]