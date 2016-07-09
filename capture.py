from time import sleep
from picamera import PiCamera

cam = PiCamera(resolution=(1280, 720), framerate=60)
#cam.awb_mode = 'off'
cam.meter_mode = 'matrix'
cam.shutter_speed = int((1/60.0) * 1000000)
cam.vflip = True
cam.iso = 64

#cam.start_preview()
#sleep(2)
#cam.stop_preview()

for filename in cam.capture_continuous('data/img-{timestamp:%Y:%m:%d::%H:%M:%s}.jpg'):
  print('Captured %s' % filename)
  sleep(30)
