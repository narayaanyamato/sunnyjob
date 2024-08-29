from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter().order_by('cname')

    

class Jobs(models.Model):
    jid=models.IntegerField()
    jpdate=models.DateField()
    jtitle=models.CharField(max_length=500)
    cname=models.CharField(max_length=30)
    edu=models.CharField(max_length=20)
    loc=models.CharField(max_length=45)
    email=models.EmailField()
    phone=models.CharField(max_length=40)
    caddress=models.CharField(max_length=100)
    objects=CustomManager()
    

