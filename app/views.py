from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

def display_country(request):
    QLCO=country.objects.all()  #To retrieve all the data in the table
    QLCO=country.objects.all().order_by('country_name')  #By Ascending order
    QLCO=country.objects.all().order_by('-country_name')  #By Descending order
    QLCO=country.objects.all().order_by(Length('country_name'))  #By Ascending order by Length
    QLCO=country.objects.all().order_by(Length('country_name').desc())  #By Descending order by Length
    QLCO=country.objects.filter(country_id = 5).order_by('country_name')  #By using filter method given ascending order
    QLCO=country.objects.all()  
    d={'country' : QLCO}
    return render(request,'display_country.html',d)


def display_capital(request):

    QLCO=capital.objects.all()
    QLCO=capital.objects.all().order_by('capital_name')
    QLCO=capital.objects.all().order_by('-capital_name')
    QLCO=capital.objects.all().order_by(Length('capital_name'))
    QLCO=capital.objects.all().order_by(Length('capital_name').desc())
    QLCO=capital.objects.filter(capital_id = 122).order_by('capital_name')
    QLCO=capital.objects.filter(capital_id__gt = 122)
    QLCO=capital.objects.filter(capital_id__lt = 122)
    QLCO=capital.objects.filter(capital_id__gte = 122)
    QLCO=capital.objects.filter(capital_id__lte = 122)
    QLCO=capital.objects.filter(capital_id__startswith = 1)
    QLCO=capital.objects.filter(capital_id__endswith = 1)
    QLCO=capital.objects.filter(capital_id__contains = 3)
    QLCO=capital.objects.filter(capital_name__regex = '\wF$')#By using regex we get regular expression values
    QLCO=capital.objects.filter(capital_id__in = [121,123])#By using slicing we can use rownum which is in sql
    QLCO=capital.objects.filter(capital_id=121,capital_name='DELHI')#By using (,) we can do and operations
    QLCO=capital.objects.filter(Q(capital_id=121) & Q(capital_name='DELHI'))#by using Q we are doing and operator
    QLCO=capital.objects.filter(Q(capital_id=121) | Q(capital_name='DELHI'))#by using Q we are doing or operator
   
    d={'capital' : QLCO}
    return render(request,'display_capital.html',d)




def insert_country(request):
    cid=int(input('Enter country id :'))
    cn=input('Enter country name :')
    NCOB=country.objects.get_or_create(country_id=cid,country_name=cn)[0]
    NCOB.save()
    QLCO=country.objects.all()
    d={'country' : QLCO}
    return render(request,'display_country.html',d)




def insert_capital(request):
    coid=int(input('enter country id:'))
    caid=int(input('Enter capital id :'))
    cname=input('Enter capital name :')
    COB=country.objects.get(country_id=coid)
    NCOB=capital.objects.get_or_create(capital_id=caid,capital_name=cname,country_id=COB)[0]
    NCOB.save()
    QLCO=capital.objects.all()
    d={'capital' : QLCO}
    return render(request,'display_capital.html',d)