import cv2

def Exception(image):
  cv2.rectangle(image, (0,0), (500,100), (0,0,0), cv2.FILLED)
  cv2.putText(image, "TRYING TO FIND HAND.." , (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255), 2, cv2.LINE_AA)