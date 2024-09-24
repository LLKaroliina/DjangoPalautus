from django.db import models
class Lihasryhmat(models.Model):
    lihasryhmanimi = models.CharField(max_length = 50, default = "lihasryhmä")  
    def __str__(self):
        return f"{self.lihasryhmanimi}" 
class Treeniliikkeet(models.Model):
    liikenimi = models.CharField(max_length = 20, default = "liike")
    paino = models.DecimalField(max_digits = 8, decimal_places= 2, default = 1.00)
    toistomaara = models.IntegerField(default = 3)
    lihasryhma = models.ForeignKey(Lihasryhmat, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.liikenimi} produced by {self.lihasryhma.lihasryhmanimi}"
class Viikonpaivat(models.Model):
    viikonpaivanimi = models.CharField(max_length = 50, default = "viikonpäivä")   
class Kestavyysliikunta(models.Model):
    liikuntalaji = models.CharField(max_length = 20, default = "laji")
    kesto = models.CharField(max_length = 20, default = "kesto")
    viikonpaiva = models.ForeignKey(Viikonpaivat, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.liikuntalaji} produced by {self.viikonpaiva.viikonpaivanimi}"    

# Create your models here.
