import serial.tools.list_ports
from roboflow import Roboflow
import json

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
count  = 0

rf = Roboflow(api_key="otKMUXAELXaU2XZsT77M")
project = rf.workspace().project("biomedical-wastes")
model = project.version(3).model

json_response = model.predict("./image.jpg", confidence=40, overlap=30).json()

portsList = []
# portvar = ""
for onePort in ports:
    portsList.append(str(onePort))
    print (str(onePort))

val = "9"

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portvar = "COM" + str(val)
        print (portvar)

serialInst.baudrate = 115200
serialInst.port = portvar
serialInst.open()

isTest= True;
while isTest:
    threshold = 0.8
    for prediction in json_response["predictions"]:
        if prediction["confidence"] > threshold:
            # Do something specific
            print("Syringe detected!")
            cmd = "INJD"
            serialInst.write(cmd.encode('utf-8'))
            isTest=False
            # save the JSON response to a file
            with open('output.json', 'w') as f:
                json.dump(json_response, f)
            break;