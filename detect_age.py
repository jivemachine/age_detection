# this script will predict age for images

# imports
import numpy as np
import argparse
import cv2
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-f", "--face", required=True, help="path to face detector model directory")
ap.add_argument("-a", "--age", required=True, help="path to age detector model directory")
ap.add_argument("-c", "--confidence", type="float", default=0.5, help="minimum probability to filter weak detections")

args = vars(ap.parse_args())

# defined buckets of age brackets our age detector will predict
AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
