#from django.urls import path
#from .views import home, error  # Import your views

#urlpatterns = [
  #  path('', home, name='home'),  # Home page
 #   path('error/', error, name='error'),  # Error page  
#]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from portfolio_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', home, name='home'),
    path('error/', error, name='error'),
    
    
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
