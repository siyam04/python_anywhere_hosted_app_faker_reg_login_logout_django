"""project_source URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('admin/', admin.site.urls),
    # Apps URLs included
    path('root/', include('first_app.urls')),
    path('root/', include('second_app_user.urls')),
    path('root/', include('third_app_forms.urls')),
    path('root/', include('fourth_app_reg_login_logout.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Project source URL Debugging integration
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns




