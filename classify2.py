#!/usr/bin/python3

# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tflite_runtime.interpreter import Interpreter
import numpy as np
import argparse
from PIL import Image
import cv2

parser = argparse.ArgumentParser(description='Image Classification')
parser.add_argument('--filename', type=str, help='Specify the filename', required=True)
parser.add_argument('--model_path', type=str, help='Specify the model path', required=True)
parser.add_argument('--label_path', type=str, help='Specify the label map', required=True)
parser.add_argument('--top_k', type=int, help='How many top results', default=3)

args = parser.parse_args()

filename = args.filename
model_path = args.model_path
label_path = args.label_path
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

img = cv2.imread('snapple.jpg')
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