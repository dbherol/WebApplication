"""Good_Driver_Incentive_Program URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from GoodDriverIncentive import views
#from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^GoodDriverIncentive/', include('GoodDriverIncentive.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    #path('accounts/', include('GoodDriverIncentive.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),  #URL pattern for login page (http://webname/accounts)
    #path('', TemplateView.as_view(template_name='home.html'), name='home'), #URL pattern for homepage
]
