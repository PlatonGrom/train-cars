# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1poNuK6bkN8RUcekENpjizfB4UPit4W4I
"""

nvidia-smi

pip install ultralytics

from ultralytics import YOLO
import os
from IPython.display import display, Image
from IPython import display
display.clear_output()
!yolo mode=checks

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="MjxSa12k4J2gOXe5GjcH")
project = rf.workspace("plats").project("cars-wchuj")
dataset = project.version(5).download("yolov8")

!yolo task=detect mode=train model=yolov8m.pt data={dataset.location}/data.yaml epochs=20 imgsz=640

Image(filename=f'/content/runs/detect/train/confusion_matrix.png', width=600)

Image(filename=f'/content/runs/detect/train/results.png', width=600)