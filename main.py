import os
import cv2
import numpy as np
from kivy.app import App
from kivy.uix.label import Label
from model import TensorFlowModel


class MyApp(App):

    def build(self):
        model = TensorFlowModel()
        model.load(os.path.join(os.getcwd(), 'model.tflite'))

        img = cv2.imread('nol.png', 0)    # Read Image
        img = np.reshape(img, [1, 30, 30, 1])  # Resize img for model. Which size model want us.
        img = np.array(img, np.float32)  # change numpy arrays int8 to float32

        y = model.pred(img)  # Predict img

        y = np.argmax(y)  # user np.argmax() -> numpy argument max function input / np.argmax([1,0,0,0,0,0,0,0,0,0]) = 0
        return Label(text=f'{y}')


if __name__ == '__main__':
    MyApp().run()
