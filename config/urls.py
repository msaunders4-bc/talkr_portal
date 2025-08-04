from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('login/', include('login.urls')),
    path('portal/', include('portal.urls', namespace='portal')),
]
