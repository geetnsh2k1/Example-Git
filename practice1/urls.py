"""practice1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.handlelogin),
    path('logout/', views.handlelogout),
    path('signup/', views.handlesignup),
    path('response/', views.handleresponse),
    path('viewallproducts/', views.viewproducts, name='allproducts'),
    path('viewallproducts/like/', views.handlelikes),
    path('addproduct/', views.addproduct),
    path('addproduct/addproductform/', views.handleaddproduct),
    path('deleteproduct/', views.deletepage),
    path('deleteproduct/deleteproductform/', views.handledeleteproduct),
    path('admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
