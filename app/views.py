from django.shortcuts import render, redirect, get_object_or_404
from .models import Treeniliikkeet, Lihasryhmat, Kestavyysliikunta, Viikonpaivat 
#from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import LihasryhmatSerializer, TreeniliikkeetSerializer, ViikonpaivatSerializer, KestavyysliikuntaSerializer


def landingview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        return render(request, 'landingpage.html')
# return render(request, 'landingpage.html')
#lOGIN 
def loginview(request):
     return render (request, 'loginpage.html')
#SAADAAN TIEDOT LOGIN.HTML
def login_action(request):
     user = request.POST['username']
     passw = request.POST['password']
     user = authenticate(username = user, password = passw)
     #ON JO TUTKITTU, ONKO KÄYTTÄJÄ OLEMEASSA. JOS ON KIRJATAAN SISÄÄN
     if user:
          login(request, user)
          context = {'name': user}
          return render(request, 'landingpage.html', context)
     #JOS KÄYTTÄJÄÄ EI LÖYDY
     else:
          return render(request, 'loginerrorpage.html')
#PUTSAA KIRJAUTUMISTIEDOT JA MENNÄÄN KIRJAUTUMISSIVULLE
def logout_action(request):
     logout(request)
     return render(request, 'loginpage.html')
#TREENI
def treeniliikkeetview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        treeniliikkeet = Treeniliikkeet.objects.all()
        lihasryhmat = Lihasryhmat.objects.all()
        context = {'treeniliikkeet': treeniliikkeet, 'lihasryhmät' : lihasryhmat}
        return render(request, 'treeniliikkeet.html', context)
def addtreeniliikkeet(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        a = request.POST['liikenimi']
        b = request.POST['paino']
        c = request.POST['toistomaara']
        d = request.POST['lihasryhma']
        Treeniliikkeet(liikenimi = a, paino = b, toistomaara = c,  lihasryhma = Lihasryhmat.objects.get(id = d)).save()
        return redirect(request.META['HTTP_REFERER'])
def confirmdeletetreeniliikkeet(request, id):
    treeniliikkeet = Treeniliikkeet.objects.get(id = id)
    context = {'treeniliikkeet': treeniliikkeet}
    return render (request,"confirmdeltre.html",context)
def deletetreeniliikkeet(request, id):
    Treeniliikkeet.objects.get(id = id).delete()
    return redirect(treeniliikkeetview)
def edit_treeniliikkeet_get(request, id):
    treeniliikkeet = Treeniliikkeet.objects.get(id = id)
    context = {'treeniliikkeet': treeniliikkeet}
    return render (request, "edit_treeniliikkeet.html", context)
def edit_treeniliikkeet_post(request, id):
        item = Treeniliikkeet.objects.get(id = id)
        item.paino = request.POST['paino']
        item.toistomaara = request.POST['toistomaara']
        item.save()
        return redirect(treeniliikkeetview)
class TreeniliikkeetViewSet(viewsets.ModelViewSet):
    serializer_class = TreeniliikkeetSerializer
    def get_queryset(self):
        queryset = Treeniliikkeet.objects.all()
        nimi = self.request.query_params.get("liikenimi")
        if nimi is not None:
            queryset = queryset.filter(liikenimi=nimi)
        return queryset
#lIHASRYHMÄT
def lihasryhmatview(request):
    lihasryhmat = Lihasryhmat.objects.all() 
    context = {'liharyhmät': lihasryhmat} #luodaan context jonka nimi on suopplierslist kaikki tietokannasta
    return render (request, "lihasryhmat.html", context)
def addlihasryhma(request):
    a = request.POST['lihasryhmanimi']
    Lihasryhmat(lihasryhmanimi = a).save()
    return redirect(request.META['HTTP_REFERER'])
class LihasryhmatViewSet(viewsets.ModelViewSet):
    serializer_class = LihasryhmatSerializer
    def get_queryset(self):
        queryset = Lihasryhmat.objects.all()
        nimi = self.request.query_params.get("lihasryhmanimi")
        if nimi is not None:
            queryset = queryset.filter(lihasryhmanimi=nimi)
        return queryset
#KESTÄVYYSLIIKUNTA
def kestavyysliikuntaview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        kestavyysliikunta = Kestavyysliikunta.objects.all()
        viikonpaivat = Viikonpaivat.objects.all()
        context = {'kestavyysliikunta': kestavyysliikunta, 'viikonpaivat' : viikonpaivat}
        return render(request, 'kestavyysliikunta.html', context)
def addkestavyysliikunta(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        a = request.POST['liikuntalaji']
        b = request.POST['kesto']
        c = request.POST['viikonpaiva']
        Kestavyysliikunta(liikuntalaji = a, kesto = b,  viikonpaiva = Viikonpaivat.objects.get(id = c)).save()
        return redirect(request.META['HTTP_REFERER'])
def confirmdeletekestavyysliikunta(request, id):
    kestavyysliikunta = Kestavyysliikunta.objects.get(id = id)
    context = {'kestavyysliikunta': kestavyysliikunta}
    return render (request,"confirmdelkest.html",context)
def deletekestavyysliikunta(request, id):
    Kestavyysliikunta.objects.get(id = id).delete()
    return redirect(kestavyysliikuntaview)
class KestavyysliikuntaViewSet(viewsets.ModelViewSet):
    serializer_class = KestavyysliikuntaSerializer
    def get_queryset(self):
        queryset = Kestavyysliikunta.objects.all()
        nimi = self.request.query_params.get("liikuntalaji")
        if nimi is not None:
            queryset = queryset.filter(liikuntalaji=nimi)
        return queryset
def edit_kestavyysliikunta_get(request, id):
    kestavyysliikunta = Kestavyysliikunta.objects.get(id = id)
    context = {'kestavyysliikunta': kestavyysliikunta}
    return render (request, "edit_kestavyysliikunta.html", context)
#KUN MUOKKAUKSET ON TEHTY JA PAINETAAN TALLENNA, TULLAAN TÄHÄN METODIIN
def edit_kestavyysliikunta_post(request, id):
        item = Kestavyysliikunta.objects.get(id = id)
        item.liikuntalaji = request.POST['liikuntalaji']
        item.kesto = request.POST['kesto']
        # item.viikonpaiva = request.POST['viikonpaiva']
        item.save()
        return redirect(kestavyysliikuntaview)    
#VIIKONPÄIVÄT
def viikonpaivatview(request):
    viikonpaivat = Viikonpaivat.objects.all() 
    context = {'viikonpaivat': viikonpaivat} #luodaan context jonka nimi on suopplierslist kaikki tietokannasta
    return render (request, "viikonpaivat.html", context)
class ViikonpaivatViewSet(viewsets.ModelViewSet):
    serializer_class = ViikonpaivatSerializer
    def get_queryset(self):
        queryset = Viikonpaivat.objects.all()
        nimi = self.request.query_params.get("viikonpaivanimi")
        if nimi is not None:
            queryset = queryset.filter(viikonpaivanimi=nimi)
        return queryset
def addviikonpaiva(request):
    a = request.POST['viikonpaivanimi']
    Lihasryhmat(viikonpaivanimi = a).save()
    return redirect(request.META['HTTP_REFERER'])


# Create your views here.
