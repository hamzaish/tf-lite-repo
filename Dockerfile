FROM nvcr.io/nvidia/l4t-base:r32.5.0

WORKDIR /project

COPY main_pir.py model2.tflite servokit.py webcam.py pir_sensor.py motors.py optimized_class.py requirements.txt ./

RUN apt-get update
RUN apt-get install -y python3.6
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN python3 --version
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN pip3 install Jetson.GPIO

RUN pip install -r requirements.txt
RUN echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | tee /etc/apt/sources.list.d/coral-edgetpu.list
RUN apt-get install -y curl
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update
RUN apt-get install -y python3-tflite-runtime
RUN DEBIAN_FRONTEND=noninteractive TZ=America/New_York apt-get install ffmpeg libsm6 libxext6 -y

CMD ["python3", "./main_pir.py"]
 
