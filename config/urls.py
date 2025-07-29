
from django.contrib import admin
from django.urls import path, include
from portal import views as index_views

urlpatterns = [
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('portal/', include('portal.urls')),
]
