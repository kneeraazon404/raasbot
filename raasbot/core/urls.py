from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login_view'),
    path('dashboard', views.dahsboard, name='dashboard'),
    path('logout', views.logout_view, name='logout_view')
]