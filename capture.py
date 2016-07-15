from time import sleep
from picamera import PiCamera
import string
import random

high=(3264,2448)
mid=(1024,768)
low=(320,240)

cam = PiCamera(resolution=mid)

#cam.awb_mode = 'off'
cam.meter_mode = 'matrix'
#cam.exposure_mode = 'night'
#cam.shutter_speed = int((1/12.0) * 1000000)
#cam.vflip = True
#cam.iso = 32 

cam.start_preview()
sleep(2)
cam.stop_preview()

seed = string.ascii_lowercase + string.digits
random_str = ''.join(random.choice(seed) for _ in range(6))
filename_prefix = '/home/pi/Desktop/cam/data/img-%s' % random_str

for filename in cam.capture_continuous(filename_prefix + "{timestamp:%Y-%m-%dT%H:%M:%S.%f%Z}-{counter:05d}.jpg"):
  print('Captured %s' % filename)
  sleep(10)
