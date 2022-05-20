"""real_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, re_path, path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('', include(('core.urls','core'), namespace='core')),
    path('management/', include('management.urls')),
    path('tenant/', include('tenant.urls')),
    re_path(r"^dashboard/", views.dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.dashboard, name="dashboard"),
    path('accounts/login/', views.login, name='login'),
    path('accounts/password-reset/', views.password_reset_form, name='password_reset_form'),
    path('accounts/password-change/', views.password_change_form, name='password_change_form')

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)