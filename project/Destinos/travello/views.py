from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.desc="The best city for visit in the summer"
    dest1.img="destination_1.jpg"
    dest1.price=700
    dest1.offer=True

    dest2=Destination()
    dest2.name="Paris"
    dest2.desc="The city of love"
    dest2.img="destination_2.jpg"
    dest2.price=680
    dest2.offer=False

    dest3=Destination()
    dest3.name="Hawai"
    dest3.desc="Beautiful city"
    dest3.img="destination_3.jpg"
    dest3.price=750
    dest3.offer=True

    dests=[dest1, dest2, dest3]

    return render(request,'index.html',{'dests': dests})