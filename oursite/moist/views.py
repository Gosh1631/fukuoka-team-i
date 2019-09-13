from django.http import HttpResponse
from django.views import View
import serial,time

# Create your views here.

# def index(request):
#     return 

class index(View):
    template_name = "moist.html"
    class response(View):
        ser = serial.Serial("/dev/cu.usbmodem14401",9600)
        rate = ser.readline()
        params = {
            "water_level": rate,
        }
        if rate() < 100:
            int.status = 0
            ser.write(1)

        elif rate() < 200:
            int.status = 1
            ser.write(0)

        else:
            int.status = 2
            ser.write(0)
        # return render(request,"moist.html",params)