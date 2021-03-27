from read_mpu6050 import *

time.sleep(1)
print('recording data...')

while True:
    try:
        gx, gy, gz, ax, ay, az = mpu6050_conv()
    except:
        continue
    
    print('Gx = {0:2.3f} Gy = {0:2.3f} Gz = {0:2.3f} Ax = {0:2.3f} Ay = {0:2.3f} Az = {0:2.3f}'.format(gx,gy,gz,ax,ay,az))
    #print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
    time.sleep(0.5)