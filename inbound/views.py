from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def api(request):
    if (request.method) == "POST":
        updated_data = request.POST.copy()
        print("Haha", updated_data)
    return