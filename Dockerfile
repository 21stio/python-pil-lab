FROM python:2.7-wheezy

WORKDIR /opt/pil-lab

COPY . .

RUN pip install pillow
RUN pip install numpy