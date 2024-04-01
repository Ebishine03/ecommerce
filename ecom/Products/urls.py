from django.urls import  path
from  .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('',views.index,name='home'),
 path('productList/',views.list_products,name='productList'),
 path('productDeatils/<pk>',views.product_details,name='productDeatils')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)