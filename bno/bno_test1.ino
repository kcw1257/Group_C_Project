#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (100) //delay between fresh examples

Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28); //i2c address

void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(115200);

  //initialise
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("No BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  else
  {
    Serial.println("BNO055 Initialised");
  }
  
  delay(1000);

  bno.setExtCrystalUse(true);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Possible vector values can be:
  // - VECTOR_ACCELEROMETER - m/s^2
  // - VECTOR_MAGNETOMETER  - uT
  // - VECTOR_GYROSCOPE     - rad/s
  // - VECTOR_EULER         - degrees
  // - VECTOR_LINEARACCEL   - m/s^2
  // - VECTOR_GRAVITY       - m/s^2
  //imu::Vector<3> NAME = bno.getVector(Adafruit_BNO055::VECTOR_NAME)

  uint8_t system, gyro, accel, mag=0 ;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  imu::Vector<3> gyros = bno.getVector(Adafruit_BNO055::VECTOR_GYROSCOPE);
  imu::Vector<3> acc = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  imu::Vector<3> magnet = bno.getVector(Adafruit_BNO055::VECTOR_MAGNETOMETER);

  //euler angle
  Serial.print("EULER: ");
  Serial.print(euler.x());
  Serial.print(",");
  Serial.print(euler.y());
  Serial.print(",");
  Serial.println(euler.z());

  //gyro
  Serial.print("GYRO: ");
  Serial.print(gyros.x());
  Serial.print(",");
  Serial.print(gyros.y());
  Serial.print(",");
  Serial.println(gyros.z());

  //accel
  Serial.print("ACCEL: ");
  Serial.print(acc.x());
  Serial.print(",");
  Serial.print(acc.y());
  Serial.print(",");
  Serial.println(acc.z());

  Serial.print("CALIBRATION: Sys=");
  Serial.print(system, DEC);
  Serial.print(" Gyro=");
  Serial.print(gyro, DEC);
  Serial.print(" Accel=");
  Serial.print(accel, DEC);
  Serial.print(" Mag=");
  Serial.println(mag, DEC);

  delay(BNO055_SAMPLERATE_DELAY_MS);
  //Serial.print("\t\t");
}
