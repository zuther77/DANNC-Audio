import os
from moviepy.editor import *
import subprocess

def extractor(a):
    b = a.split('.')
    current = os.getcwd()
    current = current + '\\media\\video\\'
    video_file = current + a
    audio_file = current + 'extracted_' + b[0] +'.mp3'
    audioclip = AudioFileClip(video_file)
    audioclip.write_audiofile(audio_file)

def noaudio(name):
    command = 'cd media & cd video & ffmpeg -i ' + name +  ' -c copy -an silent_' + name
    #command = 'cd media & ffmpeg -i ' + path +  ' -c copy -an silent_' + path
    #command = 'cd media & ffmpeg -i bruh.mp4 -vn -c:a copy soundtrack.m4a'
    print(command)
    subprocess.call(command, shell=True)


def recombine2(name):
    name_only = name.split('.')
    #command = 'ffmpeg -i silent_test.mp4 -i denoised_test.mp3 -c:v copy -c:a aac output.mp4'
    command = 'cd media & cd video & ffmpeg -i silent_test.mp4 -i denoised_test.wav' + ' -c:v copy -c:a aac denoised_' + name
    subprocess.call(command, shell= True)

    #delete silent vid and denoised.wav audio output from model
    command = 'cd media & cd video & del silent_test.mp4 & del denoised_test.wav'
    subprocess.call(command, shell= True)
    

# extractor()
# noaudio('bruh.mp4')
#recombine2('test.mp4')

