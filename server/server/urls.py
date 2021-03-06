from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('api/v1/users/', include('users.urls')),
    path('api/v1/', include('tasks.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
