from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse, Http404
from dancc.denoiser import denoise

import os

is_video = False

# Create your views here.
def home(request):
    return render(request,'dancc/index.html')

def clear_media_dir():
    current = os.getcwd()
    current = current + '\\media\\test.wav'
    os.remove(current)
    print('Deleted' , current)



def output(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.split('.')
    extension = b[1]
   
    fileObj.name = 'test.' + extension

    #saving files of media folder 
    path_to_file = fs.save(fileObj.name , fileObj)
    path = fs.url(path_to_file)

    
   
    
    #remove files uploded after download is done 
    
    
    
    #calling main.py of Unet model with media/test as input 
    d_path = '/media/' + denoise(a)
    clear_media_dir()

    context ={
        'file_name': a,
        'file_path': path,
        'download_path': d_path
    }
    return  render(request,'dancc/output.html', context)




def denoise_video_file(request):
    is_video = True
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.split('.')
    extension = b[1]
    print(extension)
    if extension == 'mp4':
        return output(request)

    else:
        return render( request , 'dancc/index.html', {'alert_flag':True})
    



def denoise_audio_file(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.lower().split('.')
    extension = b[1]
    if extension == 'mp3' or extension == 'wav':
        return output(request)

    else:
        return render( request , 'dancc/index.html', {'alert_flag':True})
    
     


def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
