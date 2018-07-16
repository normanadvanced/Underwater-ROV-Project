//Depth/Temperature library can be found here: https://github.com/bluerobotics/BlueRobotics_MS5837_Library

///For the Gyroscope////////////////////////////////////////////////////////////
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

Adafruit_BNO055 bno = Adafruit_BNO055(55);

void get_gyro_loop(){
   /* Get a new sensor event */
  sensors_event_t event;
  bno.getEvent(&event);
  Serial.print((float)event.orientation.x);
  Serial.print(F(" "));
  Serial.print((float)event.orientation.y);
  Serial.print(F(" "));
  Serial.print((float)event.orientation.z);
  Serial.print(F(" \n"));


  delay(100);
}

////////////////////////////////////////////////////////////////////////////////


///For the Bar30 Sensor/////////////////////////////////////////////////////////
#include "MS5837.h"
MS5837 sensor;


void get_p_t_loop(){
  sensor.read();
  
  Serial.print("Temperature: "); 
  Serial.print(sensor.temperature()); 
  Serial.print(" deg C  \n");
  
  Serial.print("Depth: "); 
  Serial.print(sensor.depth()); 
  Serial.print(" m  \n"); 
  Serial.print("\n");
}



////////////////////////////////////////////////////////////////////////////////


///For the Hydrophone///////////////////////////////////////////////////////////

int HydrophonePin = A0;   
int sensorValue = 0;  // variable to store the value coming from the Hydrophone
int initiate = 1;
int i = 0;
int sensorMax = 0;
int _x;

void get_ping_loop() {
  //calibrates
  if (initiate == 1){
    for (i=0; i<80; i++){
      _x = analogRead(HydrophonePin);
      if (_x > sensorMax){
        sensorMax = _x;
      }
      delay(1);
      }
    Serial.println("Done with initiate. Max Noise is");
    Serial.println(sensorMax);
    Serial.println("");
    delay(100);
    initiate = 0;
  }

    // read the value from the sensor:
  sensorValue = analogRead(HydrophonePin);
  Serial.print("Ping: ");
  Serial.print(sensorValue);
  Serial.print("\n");
  delay(1);  
}

////////////////////////////////////////////////////////////////////////////////



void setup() {
  Serial.begin(115200);
  Wire.begin();

  //Initialise the sensors
  if(!bno.begin())
  {
    /* bad connection */
    Serial.print("No BNO055 detected");
  }

  while (!sensor.init()) {
    /* Make sure to use SDA and SCL ports*/
    Serial.println("Failed!");
    Serial.println("Bad Connection, make sure you connect: White=SDA (A20,A4), Green=SCL (A21,A5)");
    delay(2000);
  }

  sensor.setModel(MS5837::MS5837_30BA);
  sensor.setFluidDensity(997); // kg/m^3 (freshwater, 1029 for seawater)
   
  delay(100);
  
  bno.setExtCrystalUse(true);
  
}

void loop(){
  
  get_gyro_loop();
  get_ping_loop();
  get_p_t_loop();

  }
  
