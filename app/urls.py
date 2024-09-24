"""
URL configuration for hyvinvointiSovellus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import landingview, treeniliikkeetview,  lihasryhmatview, kestavyysliikuntaview, viikonpaivatview
from .views import loginview, login_action, logout_action, edit_treeniliikkeet_get, edit_treeniliikkeet_post
from .views import addtreeniliikkeet, addlihasryhma, addkestavyysliikunta, addviikonpaiva, edit_kestavyysliikunta_get, edit_kestavyysliikunta_post  
from .views import deletekestavyysliikunta, confirmdeletekestavyysliikunta, deletetreeniliikkeet, confirmdeletetreeniliikkeet
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"treeniliikkeet", views.TreeniliikkeetViewSet, "liikenimi")
router.register(r"lihasryhmat", views.LihasryhmatViewSet, "id")
router.register(r"kestavyysliikunta", views.KestavyysliikuntaViewSet, "liikuntalaji")
router.register(r"viikonpaivat", views.ViikonpaivatViewSet, "viikonpaivanimi")

urlpatterns = [
    path("api/", include((router.urls, "app"))),
    path('index/', landingview),
    path('', loginview),
    #FUNKTIOT, MITKÄ TOTEUTTAVAT KIRJAUTUMISTA
    path('login/', login_action),
    path('logout/', logout_action),
    #TREENI URL'S
    path('treeniliikkeet/', treeniliikkeetview),
    path('add-treeniliikkeet/', addtreeniliikkeet),
    path('delete-treeniliikkeet/<int:id>/', deletetreeniliikkeet),
    path('confirm-delete-treeniliikkeet/<int:id>/', confirmdeletetreeniliikkeet),
    path('edit-treeniliikkeet-get/<int:id>/', edit_treeniliikkeet_get),
    path('edit-treeniliikkeet-post/<int:id>/', edit_treeniliikkeet_post),
    #LIHASRYHMÄT
    path('lihasryhmat/', lihasryhmatview),
    path('add-lihasryhma/', addlihasryhma),
    #KESTÄVYYSLIIKUNTA
    path('kestavyysliikunta/', kestavyysliikuntaview),
    path('add-kestavyysliikunta/', addkestavyysliikunta),
    path('delete-kestavyysliikunta/<int:id>/', deletekestavyysliikunta),
    path('confirm-delete-kestavyysliikunta/<int:id>/', confirmdeletekestavyysliikunta),
    path('edit-kestavyysliikunta-get/<int:id>/', edit_kestavyysliikunta_get),
    path('edit-kestavyysliikunta-post/<int:id>/', edit_kestavyysliikunta_post),
    #VIIKONPÄIVÄT
    path('viikonpaivat/', viikonpaivatview),
    path('add-viikonpaiva/', addviikonpaiva)
    
]
