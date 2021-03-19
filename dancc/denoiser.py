from dancc.prediction_denoise import prediction

def denoise():
    #Example: python main.py --mode="prediction"
    #path to find pre-trained weights / save models
    weights_path = 'E:/DANCC audio/front end/v2/website/weights'
    #pre trained model
    name_model = 'model_unet'
    #directory where read noisy sound to denoise
    audio_dir_prediction = 'E:/DANCC audio/front end/v2/website/media/'
    #directory to save the denoise sound
    dir_save_prediction = 'E:/DANCC audio/front end/v2/website/media/'
    #Name noisy sound file to denoise
    audio_input_prediction = ['test.wav']
    #Name of denoised sound file to save
    audio_output_prediction = 'denoise.wav'
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

    return audio_output_prediction
