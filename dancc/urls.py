from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home',views.home, name='dancc-home'),
    path('output_audio',views.denoise_audio_file,name='output_audio'),
    path('output_video',views.denoise_video_file,name='output_video'),
    path('output',views.output, name='output')
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)