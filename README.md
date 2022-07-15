
### Kivy Tensorflow Android build

This is a read image and predict tflite model. Running Tensorflow Lite on iOS, Android, MacOS, Windows and Linux using Python and Kivy.

### Create a Tensorflow Lite model
Create or use any tflite model.

* <a style="color: red;" >Check Neural Network input data.</a>
* You can find out what size the neural network wants to input using <a style="color: green;" >model.py/get_input_shape()</a>.

### Install Required Python packages
``` pip3 install --upgrade pip ```<br>
``` pip3 install -r requipments.txt ```

### Install adb 
We use adb for logging android python executing commands.

### Run (Windows, Linux or MacOS)
``` python3 main.py ```

### Run (Android) 
#### Connect Android device computer with usb. Open USB-Debugging.
```buildozer init ``` <br>
```buildozer -v android debug deploy run```<br>
```adb logcat | grep python```

### <a style="color: red;" >Note</a>
* Don't Change any things on .spec file
```
source.include_exts = py,png,jpg,kv,atlas,tflite

android.gradle_dependencies = 'org.tensorflow:tensorflow-lite:1.12.0','org.tensorflow:tensorflow-lite-support:0.0.0-nightly-SNAPSHOT'

requirements = python3,kivy,numpy,opencv

android.arch = arm64-v8a, armeabi-v7a
```

### if you have a question contact
#### <a style="color: 337DFF;" >azizov.rafael@birainy.com</a>
