"""
URL configuration for i_wish project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path("logout/", views.logout_views, name='logout'),
    path('wishes/', views.wish_list, name='wish_list'),
    path('user/<int:user_id>/public_wish_list/', views.public_wishlist, name='public_wish_list'),
    path('add_wish/', views.add_wish, name='add_wish'),
    path('delete_wish/<int:wish_id>/', views.delete_wish, name='delete_wish')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
