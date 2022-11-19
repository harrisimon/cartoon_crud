
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cartoons/', include('characters.urls')),
    path('voice-actors/', include('voice_actors.urls')),
]
