from django.urls import path
from .views import IndexView, submit_pagina  # Importe a view submit_pagina

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("submit_pagina/", submit_pagina, name="submit_pagina"),  # Adicione esta linha para a view submit_pagina
]
