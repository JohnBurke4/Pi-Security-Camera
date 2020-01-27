import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# Setup the camera
camera = PiCamera()
camera.resolution = (1024, 768)

# Set the GPIO Modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

# Stops the program from taking pictures unless an object is present for more than one frame
tripped = False

# This will be the current file number
fileNumber = 0

# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT)    # Trigger
GPIO.setup(pinEcho, GPIO.IN)        # Echo

try:
    # We will have the camera run forever
    while True:
        # Set trigger to False (Low)
        GPIO.output(pinTrigger, False)

        # Allow module to settle
        time.sleep(0.4)

        # Send 10us pulse to rigger
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)

        # Start the timer
        StartTime = time.time()

        # The start time is reset until the Echo pin is taken high (==1)
        while GPIO.input(pinEcho) == 0:
            StartTime = time.time()

        # Stop when the Echo pin is no longer high - the end time
        while GPIO.input(pinEcho) == 1:
            StopTime = time.time()
            # If the sensor is too close to an object, the Pi cannot
            # see the echo quickly enough, so it has to detect that
            # problem and say what has happened
            if StopTime - StartTime >= 0.04:
                print("Error, subject too close to camera")
                StopTime = StartTime
                break

        # Calculate the pulse length
        ElapsedTime = StopTime - StartTime

        # Distance pulse travelled in that time is
        # time multiplied b the speed of sound (cm/s)
        Distance = ElapsedTime * 34326

        # That was the distance there and back so halve the value
        Distance = Distance / 2

        # Set the number below to your desired value, mine was 100cm as that was the distance of the nearest wall
        if Distance < 100:
            if tripped:
                print("Intruder!")

                # Set the filename
                fileName = "footage/picture" + str(fileNumber) + ".jpg"
                fileNumber += 1
                
                # Take the picture
                camera.capture(fileName)
                
                # Reset the failsafe
                tripped = False
				
			# Set the failsafe to active
			tripped = True
        # Otherwise 
        else:
            tripped = False
            print("Nobody there")

        time.sleep(0.5)

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
