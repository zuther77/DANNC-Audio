import os
from moviepy.editor import *
import subprocess

def extractor():
    a = 'bruh.mp4'
    b = a.split('.')
    current = os.getcwd()
    current = current + '\\media\\video\\'
    video_file = current + a
    audio_file = current + 'extraced_' + b[0] +'.mp3'
    audioclip = AudioFileClip(video_file)
    audioclip.write_audiofile(audio_file)

def noaudio(path):
    command = 'cd media & cd video & ffmpeg -i bruh.mp4 -c copy -an silent_bruh.mp4'
    #command = 'cd media & ffmpeg -i ' + path +  ' -c copy -an silent_' + path
    #command = 'cd media & ffmpeg -i bruh.mp4 -vn -c:a copy soundtrack.m4a'
    print(command)
    subprocess.call(command, shell=True)


def recombine2():
    command = 'cd media & cd video & ffmpeg -i silent_bruh.mp4 -i extraced_bruh.mp3 -c copy denoised_bruh.mp4'
    subprocess.call(command, shell= True)


# extractor()
# noaudio('bruh.mp4')
# recombine2()