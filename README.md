# Pi-Security-Camera

A simple Raspberry Pi motion sensing camera written in Python3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following components to use this:

* Raspberry Pi (I used a Raspberry Pi 3b)
* Pi Camera Module v2. Available [here](https://www.raspberrypi.org/products/camera-module-v2/)
* Ultrasonic Distance Sensor (HC-SR04). Available [here](https://thepihut.com/products/ultrasonic-distance-sensor-hcsr04)
* A Breadboard
* 4 male to female jumper leads
* A 330 Ohm resistor and a 470 Ohm resistor.

Next you need to ensure that the picamera library is installed

```
sudo apt-get update
sudo apt-get install python3-camera
```

### Hardware

How to setup the hardware needed for this project.

Given the Raspberry Pi 3b pin layout as shown below:

![Raspberry Pi 3b pin layout](/images/Image2.jpg)

Then with the breadboard and the other components you need to wire the following:

![Distance Sensor Setup](/images/Image1.png)

The Camera itself slots into the top of the Raspberry Pi.

### Cloning

Simply download the security-camera.py.

## Deployment and Results

### Deployment

Either run the file using an IDLE or assuming you have python3 added to your PATH type:

```
python security-camera.py
```

## Results

A folder called "footage" should be created when running the program. This houses all the pictures taken. 

**The program will overrite old pictures every time it is restarted**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
