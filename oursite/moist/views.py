from django.http import HttpResponse
from django.views import View
import serial,time

# Create your views here.

# def index(request):
#     return 

class index(View):
    template_name = "moist.html"
    def response(request):
        ser = serial.Serial("/dev/ttyUSB0",9600)
        rate = ser.readline()
        params = {
            "water_level": rate,
        }
        judge(rate)
        return render(request,"moist.html",params)

def judge(rate):
    if rate < 100:
        int.status = 0
        ser.write(1)

    elif rate < 200:
        int.status = 1
        ser.write(0)

    else:
        int.status = 2
        ser.write(0)