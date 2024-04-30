## SafeDisp
An AI based conveyor system that utilizes image recognition capabilities to segregate bio-medical wastes into appropriate categories and keeps track of the amount of generated waste, along with ambient conditions of the room to ensure the safety and wellbeing of workers. 

### Team Members
[1.Sarath Madhav](https://github.com/Pseudozoid)   
[2.Rishi Krishna ](https://github.com/Rishi-k-s)   
[3.Roshan Cyriac](https://github.com/RoshanCy85)   
[4.Vishnu Rajagopal](https://github.com/Vishnudrm)   

### Link to Project
[GitHub](https://github.com/Pseudozoid/BinaryBreak)

### How it Works ?
The project utilises image detection capabilites provided by the Roboflow 3.0 Object Detection model from RoboFlow. The model was trained on a custom dataset. Bio-medical wastes are placed on a conveyor belt that is monitored by a camera. Upon detection of the class of contaminant (sharps, organic-waste, fluid .. etc) a partition pushes the object into it's appropriate labelled bin and updates the count to keep track of the amount and type of waste generated. Temperature and humidity sensors in the room continuously monitor environment for ensuring safe working conditions.

### Technologies used
Roboflow 3.0 Object Detection Model
Python
ESP8266
DHT11 and MQ02 sensors

### How to configure
* Clone this repository to your local machine.
* Run pip install -r requirements.txt (use virtual environment if necessary)

### How to Run
* In main.py 
    json_response = model.predict("./image.jpg", confidence=40, overlap=30).json()

  replace "./image.jpg" with the path to your image
* Run python main.py
* If a defined contaminant is detected with sufficient confidence, the coordinates of the contaminant and other details are exported to output.json

### Other Links

[Slides](https://docs.google.com/presentation/d/1NSZxJNRLEPfxkWvTta22ScGc9xkjkmOqKzJrUhBBciM/edit?usp=sharing)