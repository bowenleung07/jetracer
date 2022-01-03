from utils import preprocess
import numpy as np

STEERING_GAIN = -1 #ranges from -1 to 1
STEERING_BIAS = 0.00 #ranges from -1 to 1

car.throttle = 0.7 #ranges from 0 to 1

while True:
  image = camera.read()
  image = preprocess(image).half()
  output = model_trt(image).detach().cpu().numpy().flatten()
  x = float(output[0])
  car.steering = x * STEERING_GAIN + STEERING_BIAS
  if (abs(car.steering) < 0.20): #change the interval
    car.throttle = 0.7 #change the throttle depending on car performance
  elif (abs(car.steering) < 0.40): #change the interval
    car.throttle = 0.55 #change the throttle depending on car performance
  else: #add or delete interval if necessary
    car.throttle = 0.40 #change the throttle depending on car performance
