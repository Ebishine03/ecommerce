from django.urls import  path
from  .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

path('cart',views.show_cart,name="cart")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)