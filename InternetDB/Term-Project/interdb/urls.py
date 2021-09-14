"""interdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from inventory import views as inven_views
import inventory

from inventory.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main1/',inven_views.mainPage1),
    path('main3/',inven_views.mainPage3),
    path('product/',inven_views.productPage),

    path('login/', loginPage),
    path('customer/', customerPage),
    path('customer/<int:customer_id>', customerDetailPage),
    path('record/', recordPage),
]

