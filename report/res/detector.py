import dlib
from skimage import io

img = io.imread('imagewithface.jpg')

detector = dlib.get_frontal_face_detector()
# Run the face detector, upsampling the image 1 time to find smaller faces.
dets = detector(img,1)

print "number of faces detected: ", len(dets)
win = dlib.image_window()
win.set_image(img)
win.add_overlay(dets)

raw_input("Hit enter to continue")
