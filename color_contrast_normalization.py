import cv2

# Got the code from here: http://stackoverflow.com/questions/24341114/simple-illumination-correction-in-images-opencv-c
# Also here: http://stackoverflow.com/questions/31998428/opencv-python-equalizehist-colored-image
# And here: https://www.packtpub.com/mapt/book/Application-Development/9781785283932/2/ch02lvl1sec26/Enhancing%20the%20contrast%20in%20an%20image

img = cv2.imread('./images/ski_lift.png')

'''
According to Wikipedia: https://en.wikipedia.org/wiki/YUV
"The Y′UV model defines a color space in terms of one luma (Y′)" Where luma represents brightness
'''
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey(0)