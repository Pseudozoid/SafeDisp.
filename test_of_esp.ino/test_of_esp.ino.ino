// #include <DHT.h>
// #define DHTPIN 7 
// #define DHTTYPE DHT11  
int gasInput = A0;

// DHT dht (DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(gasInput, INPUT);
  // dht.begin();

}

void loop() {
  
  if(Serial.available()){
    String msg = Serial.readString();

    if(msg == "ON"){
      digitalWrite(BUILTIN_LED,LOW);
      Serial.write("ANte ole Wapa\n");
    }else{
      digitalWrite(BUILTIN_LED,HIGH);
    }
  }
  Serial.println( analogRead(gasInput) );
  delay(500);
 

}

