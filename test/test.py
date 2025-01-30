import cv2
import tensorflow as tf
from deepface import DeepFace

print("OpenCV Version:", cv2.__version__)
print("TensorFlow Version:", tf.__version__)
print("GPU verfügbar:", tf.config.list_physical_devices('GPU'))
