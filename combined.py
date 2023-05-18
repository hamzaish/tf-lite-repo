import cv2 as cv
import numpy as np
from tflite_runtime.interpreter import Interpreter
import numpy as np
import argparse
from PIL import Image
import cv2

cap = cv.VideoCapture(0)
_, frame = cap.read()

parser = argparse.ArgumentParser(description='Image Classification')
parser.add_argument('--filename', type=str, help='Specify the filename', required=True)
parser.add_argument('--model_path', type=str, help='Specify the model path', required=True)
parser.add_argument('--label_path', type=str, help='Specify the label map', required=True)
parser.add_argument('--top_k', type=int, help='How many top results', default=3)

args = parser.parse_args()

filename = args.filename
model_path = 'model2.tflite'
label_path = 'labels.txt'
top_k_results = args.top_k

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