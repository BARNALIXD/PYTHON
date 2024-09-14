
# Importing Libraries 
import cv2 
import mediapipe as mp 
from math import hypot 
import screen_brightness_control as sbc 
import numpy as np 


# Initializing the Model 
mpHands = mp.solutions.hands 
hands = mpHands.Hands( 
	static_image_mode=False, 
	model_complexity=1, 
	min_detection_confidence=0.75, 
	min_tracking_confidence=0.75, 
	max_num_hands=2) 

Draw = mp.solutions.drawing_utils 
