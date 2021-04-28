# Dancc-Audio

### Remove Background Noise from Audio and Video Files 

### Requirements 
- Python 3.6 or higher
  - Dowload from https://www.python.org/downloads
- FFmpeg
  - Download for your OS from https://ffmpeg.org/download.html
  - Once downloaded and installed correctly make sure ffmpeg is set as an envirnoment variable.
  - Check if ffmpeg is working by running this command in the terminal
    ``` ffmpeg -version ```
  - If it says something like ' **ffmpeg version 4.3.1 Copyright (c) 2000-2020** ', then you are good to go.

#### Python libraries required
- tensorflow 
- moviepy
- pydub
- numpy
- scipy
- librosa
- django


### Steps for Running the project
  * Open Terninal and cd into desired directory
  * Run these Commands
    * ``` git clone https://github.com/zuther77/Dancc-Audio.git ```
    * ``` cd Dancc-Audio ```
    * ``` python pip install -r requirements.txt ```
  * Once all the dependencies get installed successfully run local server by 
    * ``` python manage.py runserver ```
  * If it returns an error saying no module name ' ... ' then install that module by running ``` python -m pip install (name of module) ```
