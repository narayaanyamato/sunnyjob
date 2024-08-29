import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sunnyjob.settings')
django.setup()
from faker import Faker
from random import *
fakegen=Faker()
from sunnyapp.models import Jobs
 
lst=["BCA","MCA","MTECH","BTECH","GRADUATE"," MBA","DIPLOMA IN CS"]
def recadd(n):
    for i in range(n):
        fjid=fakegen.random_int(max=100,min=1)
        fjpdate=fakegen.date()
        fjtitle=fakegen.job()
        fcname=fakegen.company()
        fedu=fakegen.random_element(lst)
        floc=fakegen.city()
        femail=fakegen.email()
        fphone=fakegen.phone_number()
        faddress=fakegen.address()
        Jobs.objects.get_or_create(jid=fjid,jpdate=fjpdate,jtitle=fjtitle,cname=fcname,edu=fedu,loc=floc,email=femail,
        phone=fphone,caddress=faddress)

n=int(input("Enter number of rec wanto insert :"))
recadd(n)

