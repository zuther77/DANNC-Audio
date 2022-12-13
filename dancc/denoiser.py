from dancc.prediction_denoise import prediction
from pydub import AudioSegment
import os

def denoise(a,is_mp3):
    #Example: python main.py --mode="prediction"
    #path to find pre-trained weights / save models
    weights_path = os.getcwd() + '/weights'
    #pre trained model
    name_model = 'model_unet'
    #directory where read noisy sound to denoise
    audio_dir_prediction = os.getcwd() + '/media/'
    #directory to save the denoise sound
    dir_save_prediction = os.getcwd() +  '/media/'
    #Name noisy sound file to denoise
    audio_input_prediction = ['test.wav']
    #Name of denoised sound file to save
    audio_output_prediction = 'denoise_' + a +'.wav'
    # Sample rate to read audio
    sample_rate = 8000
    # Minimum duration of audio files to consider
    min_duration = 1.0
    #Frame length for training data
    frame_length = 8064
    # hop length for sound files
    hop_length_frame = 8064
    #nb of points for fft(for spectrogram computation)
    n_fft = 255
    #hop length for fft
    hop_length_fft = 63

    prediction(weights_path, name_model, audio_dir_prediction, dir_save_prediction, audio_input_prediction,
    audio_output_prediction, sample_rate, min_duration, frame_length, hop_length_frame, n_fft, hop_length_fft)

    if is_mp3:
        current = os.getcwd()
        src = current + "\\media\\denoise_" + a +".wav"
        dst =  current + "\\media\\denoise_" + a +".mp3"
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="mp3")
        os.remove(src)
        print('Deleted' , src)

    if is_mp3:
           audio_output_prediction = 'denoise_' + a +'.mp3'
#     os.remove(os.getcwd() + '/media/' + audio_input_prediction[0])
    return audio_output_prediction


def denoise_vide():
    name = 'test.wav'
    a = name.split('.')
     #Example: python main.py --mode="prediction"
    #path to find pre-trained weights / save models
    weights_path = os.getcwd() + '/weights'
    #pre trained model
    name_model = 'model_unet'
    #directory where read noisy sound to denoise
    audio_dir_prediction = os.getcwd() +  '/media/video'
    #directory to save the denoise sound
    dir_save_prediction =  os.getcwd() + '/media/video/'
    #Name noisy sound file to denoise
    audio_input_prediction = ['extracted_test.mp3']
    #Name of denoised sound file to save
    audio_output_prediction = 'denoised_test.wav'
    # Sample rate to read audio
    sample_rate = 8000
    # Minimum duration of audio files to consider
    min_duration = 1.0
    #Frame length for training data
    frame_length = 8064
    # hop length for sound files
    hop_length_frame = 8064
    #nb of points for fft(for spectrogram computation)
    n_fft = 255
    #hop length for fft
    hop_length_fft = 63

    prediction(weights_path, name_model, audio_dir_prediction, dir_save_prediction, audio_input_prediction,
    audio_output_prediction, sample_rate, min_duration, frame_length, hop_length_frame, n_fft, hop_length_fft)

    src =  dir_save_prediction + audio_output_prediction
    # dst =  dir_save_prediction + 'denoised_test.mp3'
    # sound = AudioSegment.from_mp3(src)
    # sound.export(dst, format="mp3")

    #Deleted input video
    os.remove(dir_save_prediction  + a[0] + '.mp4')
    print("Deleted" , a[0] , ".mp4")

    #delete extracted audio from vid
    os.remove(dir_save_prediction + 'extracted_' + a[0] + '.mp3')
    print("Deleted extracted_" ,a[0] ,".mp3"  )


    return audio_output_prediction



# def wav_to_mp3(a):
#     current = os.getcwd()
#     src = current + "\\media\\denoise.wav"
#     dst =  current + "\\media\\denoise_ " + a 
#     sound = AudioSegment.from_mp3(src)
#     sound.export(dst, format="mp3")
#     os.remove(src)
#     print('Deleted' , src)
#     down_path = '/media/denoise_' + a 
#     return down_path
