from django.urls import path
from . import views
from .views import home_view,form_view,signup_view,login_view,main,index,logout_view,contact_view
urlpatterns = [
path("", views.main, name="main"),
path("logout/", views.logout_view, name="logout"),
path("user/", views.index, name="user_list"),
path("home/", views.home_view, name="home"),
path("form/", views.form_view, name="form"),
path("login/", views.login_view, name="login"),
path("signup/", views.signup_view, name="signup"),
path("contact/", views.contact_view, name="contact"),


]
