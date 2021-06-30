from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('acerca_de/', views.acerca_de, name="acerca_de"),
    path('registro/', views.registro, name="registro"),
    path('login/', LoginView.as_view(template_name='tienda_online/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='tienda_online/logout.html'), name="logout"),
    path('<str:pk>/',
         views.producto_detalles, name="producto_detalles"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
