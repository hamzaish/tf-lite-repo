import cv2
import numpy as np

class ClassifyObject():
    interpreter = None
    cap = None

    def __init__(self, interpreter, cap) -> None:
        self.interpreter = interpreter
        self.cap = cap

    def getVideo(self):
        _, frame = self.cap.read()
        return frame

    def classify(self, image: None):
        input_index = self.interpreter.get_input_details()[0]["index"]
        output_index = self.interpreter.get_output_details()[0]["index"]
        if image == None:
            img = self.getVideo()/255
        else:
            img = image/255
        img = img.astype(np.float32)
        img = cv2.resize(img, (224, 224))
        test_image = np.expand_dims(img, axis=0)
        cv2.imwrite('image.jpg', test_image)
        self.interpreter.set_tensor(input_index, test_image)
        self.interpreter.invoke()
        prob = self.interpreter.get_tensor(output_index)
        print(prob[0])
        if prob[0][0] > 0.85:
            return 'recycle'
        else:
            return 'trash'
    