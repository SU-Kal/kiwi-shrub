# kiwi-shrub
Kiwigrass was made for the use case of using the computer with dyslexia or visual impairment.

# Video Example:
https://youtu.be/UuAGvb1fIvs

## Requirements:
+ Python 3.12
+ FFMPEG (Linux)

## How to use:
+ Add a piper voice model into the folder beside the main files (https://rhasspy.github.io/piper-samples/#en_GB-alan-medium)
+ Install packages with command: `pip install -r requirements.txt`
+ Then run command: `python main.py`

## To compile with pyinstaller:

build command: `pyinstaller --noconfirm --onedir --windowed --icon="./images/kiwi.ico" --add-data "./images:./images" --add-data "<path_to_env>/lib/python3.12/site-packages/piper:piper/" --add-data "<path_to_env>/lib/python3.12/site-packages/customtkinter:customtkinter/"  "./main.py"`
