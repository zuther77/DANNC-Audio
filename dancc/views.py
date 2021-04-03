from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.http import HttpResponse, Http404
from dancc.denoiser import denoise , denoise_vide
from pydub import AudioSegment
from dancc.audio_extractor import *
import os


# Create your views here.
def home(request):
    return render(request,'dancc/index.html')

def clear_media_dir(is_mp3):
    current = os.getcwd()
    if is_mp3:
        current = current + '\\media\\test.mp3'
    else:
        current = current + '\\media\\test.wav'
    os.remove(current)
    print('Deleted' , current)


def mp3_to_wav():
    current = os.getcwd()
    src = current + '\\media\\test.mp3'
    dst =  current + "\\media\\test.wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

def wav_to_mp3(a):
    current = os.getcwd()
    src = current + "\\media\\denoise_" + a +".wav"
    dst =  current + "\\media\\denoise_ " + a +".mp3"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="mp3")
    os.remove(src)
    print('Deleted' , src)
    return 'denoise_' + a + '.mp3'


def output_audio(request):
    is_mp3 = False
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.split('.')
    extension = b[1]
    fileObj.name = 'test.' + extension
    #saving files of media folder 
    path_to_file = fs.save(fileObj.name , fileObj)
    path = fs.url(path_to_file)

    if extension == 'mp3':
        is_mp3 = True
        mp3_to_wav()
    else:
        is_mp3 = False
    
    #calling main.py of Unet model with media/test as input 
    d_path = '/media/' + denoise(b[0],is_mp3)
    clear_media_dir(is_mp3)


    context ={
        'file_name': a,
        'file_path': path,
        'download_path': d_path
    }
    return  render(request,'dancc/output.html', context)



def output_video(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage(location= settings.MEDIA_ROOT +'/video' , base_url= settings.MEDIA_ROOT +'/video')
    a = fileObj.name
    b = a.lower().split('.')
    extension = b[1]
    fileObj.name = 'test.' + extension
    #saving files of media folder 
    path_to_file = fs.save(fileObj.name , fileObj)
    path = fs.url(path_to_file)
    
    extractor(fileObj.name)
    noaudio(fileObj.name)
    denoise_vide()
    recombine2(a)

    context ={
        'file_name': a,
        'file_path': path,
        'download_path': '/media/' + 'video/denoised_' + a
    }
    return  render(request,'dancc/output.html', context)

def denoise_video_file(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.lower().split('.')
    extension = b[1]
    if extension == 'mp4':
        return output_video(request)

    else:
        return render( request , 'dancc/index.html', {'alert_flag':True})
    



def denoise_audio_file(request):
    fileObj = request.FILES['file_name']
    fs = FileSystemStorage()
    a = fileObj.name
    b = a.lower().split('.')
    extension = b[1]
    if extension == 'mp3' or extension == 'wav':
        return output_audio(request)

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
