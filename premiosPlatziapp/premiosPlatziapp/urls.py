
from django.contrib import admin
from django.urls import path, include

# urlpatterns: contiene una serie de elementos que se crean a partir de la función path los cuales
# nos permiten acceder a las vistas
urlpatterns = [
    path('admin/', admin.site.urls),
    path("polls/", include("polls.urls")) #incluirá todos las urls que encuentre urls.py en polls
]
