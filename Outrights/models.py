from django.db import models
from import_export import widgets
from django.utils import timezone

class Data(models.Model):
    def __str__(self):
        return self.date

    date=models.CharField(null=True,max_length=20,unique=True)
    h10=models.FloatField(null=True,blank=True)
    m10=models.FloatField(null=True,blank=True)
    u10=models.FloatField(null=True,blank=True)
    z10=models.FloatField(null=True,blank=True)
    h11=models.FloatField(null=True,blank=True)
    m11=models.FloatField(null=True,blank=True)
    u11=models.FloatField(null=True,blank=True)
    z11=models.FloatField(null=True,blank=True)
    h12=models.FloatField(null=True,blank=True)
    m12=models.FloatField(null=True,blank=True)
    u12=models.FloatField(null=True,blank=True)
    z12=models.FloatField(null=True,blank=True)
    h13=models.FloatField(null=True,blank=True)
    m13=models.FloatField(null=True,blank=True)
    u13=models.FloatField(null=True,blank=True)
    z13=models.FloatField(null=True,blank=True)
    h14=models.FloatField(null=True,blank=True)
    m14=models.FloatField(null=True,blank=True)
    u14=models.FloatField(null=True,blank=True)
    z14=models.FloatField(null=True,blank=True)
    h15=models.FloatField(null=True,blank=True)
    m15=models.FloatField(null=True,blank=True)
    u15=models.FloatField(null=True,blank=True)
    z15=models.FloatField(null=True,blank=True)
    h16=models.FloatField(null=True,blank=True)
    m16=models.FloatField(null=True,blank=True)
    u16=models.FloatField(null=True,blank=True)
    z16=models.FloatField(null=True,blank=True)
    h17=models.FloatField(null=True,blank=True)
    m17=models.FloatField(null=True,blank=True)
    u17=models.FloatField(null=True,blank=True)
    z17=models.FloatField(null=True,blank=True)
    h18=models.FloatField(null=True,blank=True)
    m18=models.FloatField(null=True,blank=True)
    u18=models.FloatField(null=True,blank=True)
    z18=models.FloatField(null=True,blank=True)
    h19=models.FloatField(null=True,blank=True)
    m19=models.FloatField(null=True,blank=True)
    u19=models.FloatField(null=True,blank=True)
    z19=models.FloatField(null=True,blank=True)


