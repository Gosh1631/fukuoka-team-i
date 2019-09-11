from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello,world.")

# def response(request):
#     context = {
#         if rate < 100:
#             "humid_res" = "水量が減少しています。"

#         elif rate < 200:
#             "humid_res" = "良好です。"

#         else:
#             "humid_res" = "水分量が過多になっています。"
#     }
#     return render(request, "moist":"moist.html", context)