from django.urls import path
from .views import IndexView, SubmitPaginaView  # Importe a classe SubmitPaginaView

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("submit_pagina/", SubmitPaginaView.as_view(), name="submit_pagina"),  # Use SubmitPaginaView.as_view()
]
