import pyttsx3
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (305, 480)

KV = """
MDFloatLayout:
    MDLabel:
        text: "Talk that Talk"
        pos_hint:{"center_y": .80}
        halign: "center"
        bold: True
        font_style: "H3"
    MDTextField:
        id: text
        hint_text: "Enter the text to be speak"
        size_hint_x: .8
        pos_hint:{"center_x": .5, "center_y": .5}
    MDRaisedButton:
        text: "Speak"
        size_hint_x: .5
        pos_hint:{"center_x": .5, "center_y": .35}
        on_release: app.speak()
"""
class TTTApp(MDApp):
    engine = pyttsx3.init('sapi5')
    def build(self):
        kv = Builder.load_string(KV)
        return kv
    
    def speak(self):
        self.engine.say(self.root.ids.text.text)
        self.engine.runAndWait()
    
if __name__ == "__main__":
    app = TTTApp()
    app.run()