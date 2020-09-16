from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
import time
def index(request):
    return render(request, 'pages/home.html')


def cmt(request):
    if request.method == "POST":
        uploaded_file = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        data = {
            "info": {
                "maso": "",
                "hoten": "",
                "ngaysinh": "",
                "nguyenquan": "",
                "diachi": "",
            }
        }
        time.sleep(5)
        return JsonResponse(data)
