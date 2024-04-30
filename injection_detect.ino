int redPin = D1;    // Pin for red LED
int greenPin = D2;  // Pin for green LED
int bluePin = D3;   // Pin for blue LED

void setup() {
  Serial.begin(115200);
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  digitalWrite(greenPin,HIGH);
  delay(1000);
  digitalWrite(greenPin,LOW);

}

void loop(){
  digitalWrite(redPin,LOW);
  delay(500);
  digitalWrite(greenPin,LOW);
  delay(500);
  digitalWrite(bluePin,LOW);



  if(Serial.available()){
    String msg = Serial.readString();
    if(msg == "INJD"){
      digitalWrite(redPin,HIGH);
      digitalWrite(greenPin,LOW);
      digitalWrite(bluePin,LOW);
      Serial.print("Injection Detected");
      delay(2000);
    }else{
      // digitalWrite(BUILTIN_LED,HIGH);
      Serial.print("no issue");

    }
  }


}