
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path,include
from home import views

#Django site coustimization
admin.site.site_header = "Login to Devloper Chirag"
admin.site.site_title = "Welcome to Chirag's Dashboard"
admin.site.index_title = "Welcome to this portal"


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('form', views.form, name='form')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)