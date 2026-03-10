import os
from time import sleep
import copykitten as ck
from piper import PiperVoice
import wave
import pygame
import glob
import threading
import sys



class Tts:
    def __init__(self):
        self.base_dir = None
        self.current_text = None
        self.tts_text = None
        self.voice = None
        self.text_updated = None
        self.config()
        pygame.mixer.init()

    def config(self):
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) if getattr(sys, "frozen", False) else (
        os.path.dirname(__file__))

        files = glob.glob(self.base_dir + '/*.onnx*')
        for file in files:
            if "json" not in file and ".onnx" in file:
                print(f"Model file found: {file}")
                model_path = file
            elif "json" in file and ".onnx" in file:
                print(f"Model file found: {file}")
                model_config_path = file
            else:
                pass

        if model_path is None or model_config_path is None:
            raise Exception("Config and model not found.")

        self.voice = PiperVoice.load(model_path, model_config_path)

    def tts_stop(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except:
            print("Sound is likely not alive yet. Be patient.")

    def speak_button_press(self):
        self.tts_speak()
        sleep(0.05)


    def tts_speak(self):
        pygame.mixer.music.load(os.path.join(self.base_dir, 'tts.wav'))
        pygame.mixer.music.play()

    def tts_synthesize(self):
        try:
            with wave.open("tts.wav", "wb") as wav_file:
                self.voice.synthesize_wav(self.current_text, wav_file)

        except Exception as e:
            print(e)


    def run(self):

        def thread_run():

            while True:
                try:
                    self.tts_text = ck.paste()
                except:
                    print("Paste went bwoink")

                if self.tts_text != self.current_text:
                    self.current_text = self.tts_text
                    self.text_updated(self.current_text)
                    self.tts_stop()
                    self.tts_synthesize()
                    self.tts_speak()
                sleep(0.3)

        threading.Thread(target=thread_run, daemon=True).start()
