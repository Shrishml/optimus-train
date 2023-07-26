# FROM nvidia/cuda:11.7.0-runtime-ubuntu20.04
#FROM nvidia/cuda:11.7.0-devel-ubuntu20.04
FROM nvidia/cuda:11.8.0-devel-ubuntu20.04
USER root
RUN apt-get update && apt-get install -y python3 python3-pip sudo
RUN apt-get -y update
RUN apt-get -y install git

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

COPY . /app

RUN chmod +x start_training.sh
RUN chmod +x start_training.py
RUN chmod +x start_training_a100.sh


#az devops user show --user shrish.mishra@themathcompany.com --organization https://dev.azure.com/MathCo-Innovation/



# python3 cache_data.py
# RUN apt-get install dos2unix
# RUN apt-get -y update
# RUN dos2unix start_training.sh
CMD ["python3", "start_training.py"]
