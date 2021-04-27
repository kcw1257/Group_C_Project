from read_mpu6050 import *
import smbus
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt
import cairo

plt.style.use('ggplot')

time.sleep(1)

ii = 1000 #number of points
t1 = time.time() #calculating sample rate

mpu6050_str = ['accel_x', 'accel_y', 'accel_y', 'gyro_x', 'gyro_y', 'gyro_z']
mpu6050_vec = []
t_vec = []

print('recording data')
for ii in range (0, ii):
    try:
        Gx,Gy,Gz,Ax,Ay,Az = mpu6050_conv()
        
    except:
        continue
    
    t_vec.append(time.time())
    mpu6050_vec.append([Gx,Gy,Gz,Ax,Ay,Az])
    
rate = ii/(time.time()-t1)
print('sample rate accel: {} Hz'.format(rate))
t_vec = np.subtract(t_vec, t_vec[0])

#2 subplots
fig, axs = plt.subplots(2, 1, figsize = (12,7), sharex = True)
cmap = plt.cm.Set1

ax = axs[0] #plot accelerometer data
for zz in range (0, np.shape(mpu6050_vec)[1]-3):
    data_vec = [ii[zz] for ii in mpu6050_vec]
    ax.plot(t_vec, data_vec, label=mpu6050_str[zz], color=cmap(zz))
    
ax.legend(bbox_to_anchor=(1.12, 0.9))
ax.set_ylabel('Acceleration [g]', fontsize=12)

ax2 = axs[1] #plot gyro data
for zz in range (3, np.shape(mpu6050_vec)[1]):
    data_vec = [ii[zz] for ii in mpu6050_vec]
    ax2.plot(t_vec, data_vec, label=mpu6050_str[zz], color=cmap(zz))
    
ax2.legend(bbox_to_anchor=(1.12, 0.9))    
ax2.set_ylabel('Angular Velocity[deg/s]', fontsize=12)
ax2.set_xlabel('Time[s]', fontsize=14)

fig.align_ylabels(axs)
ax.set_title(label = 'MPU6050 Output without Offset Compensation at {0:3.0f} Hz'.format(rate))
plt.show()
    
    
    
    
    