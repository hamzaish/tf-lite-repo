import cv2 as cv
import numpy as np
from tflite_runtime.interpreter import Interpreter
import numpy as np

cap = cv.VideoCapture(0)
_, frame = cap.read()

model_path = 'model2.tflite'
label_path = 'labels.txt'
top_k_results = 3

with open(label_path, 'r') as f:
    labels = list(map(str.strip, f.readlines()))                                       

# Load TFLite model and allocate tensors
interpreter = Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]

img = frame/255
img = img.astype(np.float32)
img = cv.resize(img, (224, 224))
test_image = np.expand_dims(img, axis=0)
cv.imwrite('image.jpg', test_image)
interpreter.set_tensor(input_index, test_image)
interpreter.invoke()
prob = interpreter.get_tensor(output_index)
print(prob[0])
if prob[0][0] > 0.85:
  print('recycle')
else:
  print('trash')