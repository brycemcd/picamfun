from time import sleep
from picamera import PiCamera

high=(3264,2448)
mid=(1024,768)
low=(320,240)

cam = PiCamera(resolution=mid, framerate=60)

#cam.awb_mode = 'off'
cam.meter_mode = 'matrix'
#cam.exposure_mode = 'night'
#cam.shutter_speed = int((1/12.0) * 1000000)
#cam.vflip = True
#cam.iso = 32 

cam.start_preview()
sleep(2)
cam.stop_preview()

for filename in cam.capture_continuous('/home/pi/Desktop/cam/data/img-{timestamp:%Y-%m-%dT%H:%M:%S.%f%z}.jpg'):
  print('Captured %s' % filename)
  sleep(10)
