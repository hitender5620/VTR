
import cv2
     
cam = cv2.VideoCapture(0)
img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
         print("failed to grab frame")
         break
    cv2.imshow("Live", frame)
     
    k = cv2.waitKey(1)
    if k%256 ==27:
         print("closing..")
         break
    if k%256 ==32:
         img_name = "static/image/opencv_frame_{}.png".format(img_counter)
         cv2.imwrite(img_name, frame)
         print("{}written".format(img_name))
         img_counter +=1
cam.release()
cv2.destroyAllWindows() 