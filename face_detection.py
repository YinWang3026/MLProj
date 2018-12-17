# import the necessary packages
import numpy as np
import cv2
import os

image_path = 'images'

def save_faces(cascade, imgname):
    img = cv2.imread(os.path.join(image_path, imgname))
    for i, face in enumerate(cascade.detectMultiScale(img)):
        x, y, w, h = face
        sub_face = img[y:y + h, x:x + w]
        cv2.imshow('sub_face', sub_face)
        cv2.waitKey(0)
        cv2.imwrite(os.path.join("faces", "{}_{}.jpg".format(imgname, i)), sub_face)

face_cascade = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(face_cascade)
    # Iterate through files
for f in [f for f in os.listdir(image_path) if os.path.isfile(os.path.join(image_path, f))]:
    print(f)
    save_faces(cascade, f)



