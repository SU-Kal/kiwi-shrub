from app import App
from tts import Tts
import os

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(__file__)
    image_path = os.path.join(BASE_DIR, "images")
    tts = Tts()
    app = App(tts, image_path)
    app.mainloop()