import numpy as np
from imutils.video import VideoStream
# import tensorflow as tf
import cv2
import pathlib
import time

vs = VideoStream(src = 0).start()
frame = vs.read()
time.sleep(3)
cv2.imwrite('image.jpg', frame)


"""
with open('model2.tflite', 'rb') as fid:
    tflite_model = fid.read()
    
interpreter = tf.lite.Interpreter(model_content=tflite_model)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

img = cv2.imread('/content/IMG_3488.jpg')
img = img/255
img = img.astype(np.float32)
img = cv2.resize(img, (224, 224))
test_image = np.expand_dims(img, axis=0)
cv2.imwrite('image.jpg', test_image)
interpreter.set_tensor(input_index, test_image)
interpreter.invoke()
prob = interpreter.get_tensor(output_index)
print(prob[0])
if prob[0][0] > 0.85:
  print('recycle')
else:
  print('trash')

"""
