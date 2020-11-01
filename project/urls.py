from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # django admin
    path('', include('pages.urls')),  # local apps
    path('accounts/', include('django.contrib.auth.urls'))  # user management
]
