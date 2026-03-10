import platform
import customtkinter as ctk
import os


class App(ctk.CTk):
    def __init__(self, tts, image_path):
        super().__init__()
        self.scale = self.get_scaling()
        self.geometry("600x260")
        self.images_path = image_path
        self.title("KiwiShrub")
        self.tts = tts
        self.root_height = self.winfo_height()
        self.root_width = self.winfo_width()
        self.protocol("WM_DELETE_WINDOW", self._stop_program)
        ctk.set_appearance_mode("dark")

        if platform.system() == "Windows":
            self.iconbitmap(os.path.join(self.images_path, "kiwi.ico"), default=os.path.join(self.images_path, "kiwi.ico"))
        else:
            self.iconbitmap(f'@{os.path.join(self.images_path, "kiwi.xbm")}')


        # Callback for when the text is updated
        self.tts.text_updated = self.update_text

        self.label = ctk.CTkLabel(self, text="Welcome to KiwiShrub!")
        self.label.grid(row = 0, column = 0, padx = 30, pady = 15)

        self.textbox = ctk.CTkTextbox(master=self, scrollbar_button_color='#FFCC70', corner_radius=16, border_color="#FFFFFF",
                                      border_width=2, width=int(540), height=int(100))
        self.textbox.grid(row = 1, column = 0, columnspan = 4, padx = 30)

        self.speak_button = ctk.CTkButton(master=self, corner_radius=16, text="📢", font=("Arial", 30), text_color="#000000",
                                          fg_color="#1FA358", height=50, width=75, command=self.speak_button_click)
        self.speak_button.grid(row = 2, column = 0, padx = 30, pady = 15)

        self.stop_button = ctk.CTkButton(master=self, corner_radius=16, text="🛑", font=("Arial", 30), fg_color="#A03120",
                                         text_color="#000000", height=50, width=75, command=self.stop_button_click)
        self.stop_button.grid(row = 2, column = 3, padx = 45, pady = 15)


        self.tts.run()

    def _stop_program(self):
        self.destroy()
        raise SystemExit

    def speak_button_click(self):
        self.tts.tts_stop()
        self.tts.speak_button_press()

    def stop_button_click(self):
        self.tts.tts_stop()

    def update_text(self, new_text):
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", new_text)

    def get_scaling(self):
        scaling = self._get_window_scaling()
        return scaling

    def update_scaling(self):
        self.scale = self.get_scaling()
