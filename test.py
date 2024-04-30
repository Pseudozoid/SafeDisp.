



    







from roboflow import Roboflow
import json
rf = Roboflow(api_key="otKMUXAELXaU2XZsT77M")
project = rf.workspace().project("biomedical-wastes")
model = project.version(3).model
count = 0;
# infer on a local image
json_response = model.predict("./syringe.jpg", confidence=40, overlap=30).json()

threshold = 0.8
for prediction in json_response["predictions"]:
    if prediction["confidence"] > threshold:
        # Do something specific
        print("Syringe detected!")
        break;

# save the JSON response to a file
with open('output.json', 'w') as f:
    json.dump(json_response, f)





