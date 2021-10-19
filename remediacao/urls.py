from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('remediacao.pages.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    
 ]