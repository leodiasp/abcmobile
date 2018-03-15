from django.conf.urls import url, include
from .views import *
from portal.views import *
from mobile.views import *
from admin import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^index/', index,    name='index'),
    url(r'^dashboard/', dashboard,    name='dashboard'),

]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
