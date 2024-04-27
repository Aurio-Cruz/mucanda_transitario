from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UsuarioCreate, SuccessView

urlpatterns = [
    path("", auth_views.LoginView.as_view(template_name='usuarios/login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("registar/", UsuarioCreate.as_view(), name="registar"),
    path("success/", SuccessView.as_view(), name="sucesso"),
]


