from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom error handler
handler404 = 'portfolio_app.views.error'
