import cv2
from datetime import datetime

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

rval, frame = vc.read()

fourcc = cv2.VideoWriter_fourcc(*'jpeg')
out = cv2.VideoWriter('output.mov',fourcc, 20.0, (1280,720))

while True:

  now = datetime.now()
  print(now)
  if frame is not None:   
     cv2.imshow("preview", frame)
  rval, frame = vc.read()

  # Use the code below if I need find the dimensions of the video
  '''
  height, width, channels = frame.shape
  print(height)
  print(width)
  '''
  out.write(frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break