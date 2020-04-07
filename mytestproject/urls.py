from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('animalcrossingnews/', include('animalcrossingnews.urls')),
    path('admin/', admin.site.urls),
]