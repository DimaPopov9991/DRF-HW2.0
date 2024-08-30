"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from apps.auto_parks.views import AutoparkAddCarView, AutoParksView
from apps.first.views import CarlistCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars/', CarlistCreateView.as_view(), name='cars'),
    path('cars/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='cars'),
    path('auto_park/<int:pk>/cars',AutoparkAddCarView.as_view(), name='auto_park'),

    path('users/',include('apps.users.urls')),
    path('auth/', include('apps.auth.urls')),

]
