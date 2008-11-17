/*
 * Displays text sent over the serial port (e.g. from the Serial Monitor) on
 * an attached LCD.
 */
 
#include "WProgram.h"
void setup();
void loop();
void handle();
void togglePinLight();
int thePinMode = HIGH;

void handle();

void setup()
{
  Serial.begin(9600);

	int pin = 13;
	pinMode(pin, OUTPUT);
	digitalWrite(pin, thePinMode);
}

void loop()
{
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // read all the available characters
    while (Serial.available() > 0) {
		Serial.read();
		handle();
    }
  }
}

void handle(){
	togglePinLight();
}

void togglePinLight(){
	if(thePinMode == HIGH){
		thePinMode = LOW;
	}else{
		thePinMode = HIGH;
	}
	
	digitalWrite(13,thePinMode);
}

int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

