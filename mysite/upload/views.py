from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
# from src.cardDetection import extractInfoFromImage
from upload.src.cardDetection import extractInfoFromImage


def index(request):
    return render(request, 'pages/home.html')


def cmt(request):
    if request.method == "POST":
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        data = {
            "info": {
                "maso": "N/A",
                "hoten": "N/A",
                "ngaysinh": "N/A",
                "nguyenquan": "N/A",
                "diachi": "N/A",
            }
        }

        # process
        return JsonResponse(data)
