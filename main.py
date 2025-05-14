# main.py
import cv2
import threading
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from plyer import notification
import playsound
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
ALARM_SOUND = "alarm.mp3"

def play_alarm():
    playsound.playsound(ALARM_SOUND)

class CamApp(App):
    def build(self):
        self.img = Image()
        self.capture = cv2.VideoCapture(0)
        self.last_alert = 0
        Clock.schedule_interval(self.update, 1.0/30.0)
        return self.img

    def update(self, dt):
        ret, frame = self.capture.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0 and time.time() - self.last_alert > 5:
            threading.Thread(target=play_alarm).start()
            self.last_alert = time.time()

        buf = cv2.flip(frame, 0).tobytes()
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        self.img.texture = texture

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    CamApp().run()
