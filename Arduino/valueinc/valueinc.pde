/*
 * Displays text sent over the serial port (e.g. from the Serial Monitor) on
 * an attached LCD.
 */
 
int defaultPinMode = LOW;

void handle();

void setup()
{
  Serial.begin(9600);

        pinMode(0, OUTPUT);
        pinMode(1, OUTPUT);
        pinMode(2, OUTPUT);
        pinMode(3, OUTPUT);
        pinMode(4, OUTPUT);
        pinMode(5, OUTPUT);
        pinMode(6, OUTPUT);
        pinMode(7, OUTPUT);
        pinMode(8, OUTPUT);
        pinMode(9, OUTPUT);
        pinMode(10, OUTPUT);
        pinMode(11, OUTPUT);
        pinMode(12, OUTPUT);
        pinMode(13, OUTPUT);
        digitalWrite(0, defaultPinMode);
        digitalWrite(1, defaultPinMode);
        digitalWrite(2, defaultPinMode);
        digitalWrite(3, defaultPinMode);
        digitalWrite(4, defaultPinMode);
        digitalWrite(5, defaultPinMode);
        digitalWrite(6, defaultPinMode);
        digitalWrite(7, defaultPinMode);
        digitalWrite(8, defaultPinMode);
        digitalWrite(9, defaultPinMode);
        digitalWrite(10, defaultPinMode);
        digitalWrite(11, defaultPinMode);
        digitalWrite(12, defaultPinMode);
        digitalWrite(13, defaultPinMode);
}

void loop()
{
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // read all the available characters
    char input = 'X';
    while (Serial.available() > 0) {
		input = Serial.read();
		if (input != 'S'){
                  //setPin();
                  digitalWrite(13, HIGH);
                  delay(100);
                  digitalWrite(13, LOW);
                }
                if (input == 'R'){
                  // readPin();
                }
    }
  }
}

void setPin(){
  char type = 'D';
  char pin0 = '0';
  char pin1 = '0';
  char value = 'L';
  int pin = 0;
  
  type = Serial.read();
  pin0 = Serial.read();
  pin1 = Serial.read();
  value = Serial.read();
  
  pin = ( int(pin0) * 10 ) + int(pin1);
  
  if(type == 'D'){
    if(value == 'L'){
      digitalWrite(pin, LOW);
    }else{
      digitalWrite(pin, HIGH);
    }
  }    
}
