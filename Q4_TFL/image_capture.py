import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (480, 360)

for i in range(15):
    camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
    time.sleep(5)
    camera.capture('./captured_images/19mcme16_img/19mcme16_pic'+str(i)+'.jpg')
    camera.stop_preview()
    time.sleep(5)
    
camera.close()