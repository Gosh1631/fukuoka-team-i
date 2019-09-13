from django.http import HttpResponse
import serial,time

# Create your views here.
def index(request):
    return HttpResponse("Hello,world.")

def response(request):
    ser = serial.Serial("/dev/ttyUSB0",9600)
    if rate < 100:
        int status = 0
        ser.write(1)

    elif rate < 200:
        int status = 1
        ser.write(0)

    else:
        int status = 2
        ser.write(0)
    return render(request, "moist":"moist.html", context)