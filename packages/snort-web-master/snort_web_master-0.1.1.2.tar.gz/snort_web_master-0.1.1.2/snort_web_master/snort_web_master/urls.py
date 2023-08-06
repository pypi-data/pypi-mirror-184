"""snort_web_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from snort.views import get_rule, get_rule_keys
admin.site.site_header = 'snort web master'

urlpatterns = [
    path("get_rule_update/<int:rule_id>/", get_rule),
    path("get_rule_keywords/<int:rule_id>/", get_rule_keys),
    path("", admin.site.urls),
    path('admin/', admin.site.urls),
]
