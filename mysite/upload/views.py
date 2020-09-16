from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return render(request, 'pages/home.html')


def cmt(request):
    if request.method == "POST":
        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        data = {
            "name": "",
        }
        return JsonResponse(data)
