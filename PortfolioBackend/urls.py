
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Api.urls')),  # Include the URLs from the Api app
    path('blog/', include('Blog.urls')),  # Include the URLs from the Blog app
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)