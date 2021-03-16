from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'dancc/index.html')

def output(request):
    return render(request,'dancc/output.html')


def denoise_video_file(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.split('.')
    extension = b[1]
    print(extension)
    if extension == 'mp4':
        fileObj.name = 'test.' + extension
        fs.save(fileObj.name , fileObj)

    else:
        return render( request , 'dancc/index.html', {'alert_flag':True})
    return output(request)


# def denoise_audio_file(request):
#     form = UploadForm(request.POST or None, request.FILES or None)
#     if request.is_ajax():
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'message':'hell yeah'})
#     context = {
#         'form':form,
#     }
#     return output(request)

def denoise_audio_file(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.lower().split('.')
    extension = b[1]
    if extension == 'mp3' or extension == 'wav':
        fileObj.name = 'test.' + extension
        fs.save(fileObj.name , fileObj)
    else:
        return render( request , 'dancc/index.html', {'alert_flag':True})
    return output(request)
     