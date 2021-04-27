#calibrate test 1

import smbus
from time import sleep

#some MPU6050 registers from datasheet
PWR_MGMT_1   = 0X6B #configure power mode, clock source, reset and temp disable
SMPLRT_DIV   = 0x19 #specifies divider from gyro out rate used to generate smaple rate (FIFO + DMP)
CONFIG       = 0x1A #configures Frame Synchronisation (FSYNC) pin sampling and Digital LP Filter
GYRO_CONFIG  = 0x1B #trigger self-test and full scale range
INT_ENABLE   = 0x38 #interrupt
ACCEL_XOUT_H = 0x3B # _H contain high bytes - 8 most significant bits
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

#sample rate = gyro output rate/ (1+SMPLRT_DIV)
#gyro output rate = 8kHz with DLPF disabled, 1kHz when DLPF enabled
#FS_SEL = 0 --> +/-250deg/s --> sensitivity: 131LSB/deg/s
#XG_ST, YG_ST, ZG_ST self test in x,y,z
#AFS_SEL = 0 --> +/- 2g --> sensitivty: 16384/g

def MPU_INIT():
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7) #sample rate
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    bus.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def READ_RAW(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)

    #concatenate high low value
    val = ((high << 8)| low)

    #signed value
    if (val > 32768):
        val = val - 65536
    return val

bus = smbus.SMBus(1)
Device_Address = 0x68 #i2c address

#begin initialise
MPU_INIT()
print("reading data of gyro and accelerometer")

while True:

    #read accel raw value
    accel_x = READ_RAW(ACCEL_XOUT_H)
    accel_y = READ_RAW(ACCEL_YOUT_H)
    accel_z = READ_RAW(ACCEL_ZOUT_H)

    #read gyro raw value
    gyro_x = READ_RAW(GYRO_XOUT_H)
    gyro_y = READ_RAW(GYRO_YOUT_H)
    gyro_z = READ_RAW(GYRO_ZOUT_H)

    #AFS_SEL = 0 --> +/- 2g --> sensitivty: 16384/g
    #FS_SEL = 0 --> +/-250deg/s --> sensitivity: 131LSB/deg/s

    Ax = accel_x/16384.0
    Ay = accel_y/16384.0
    Az = accel_z/16384.0

    Gx = gyro_x/131.0
    Gy = gyro_x/131.0
    Gz = gyro_x/131.0

#set MPU offsets
