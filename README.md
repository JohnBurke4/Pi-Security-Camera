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

How to setup the hardware needed for this project

Given the Raspberry Pi 3b pin layout as shown below:

![Raspberry Pi 3b pin layout](https://github.com/JohnBurke4/Pi-Security-Camera/edit/master/images/Image2.jpg)

Then with the breadboard and the other components you need to wire the following:

![Distance Sensor Setup](https://github.com/JohnBurke4/Pi-Security-Camera/edit/master/images/Image1.png)





Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
