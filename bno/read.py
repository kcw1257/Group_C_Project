import serial
import time

#arduinoData == serial.Serial('COM5', 115200)
#time.sleep(1)

try:
    arduino = serial.Serial('COM5', timeout = 1, baudrate=115200)
except:
    print("Check port")
    quit()


count = 0

while count < 100:
    dataPacket = arduino.readline()
    data_packet = str(dataPacket, 'utf-8')
    #split_packet = dataPacket.split()
    #print(split_packet)
    #x = float(split_packet[0])
    #y = float(split_packet[1])
    #z = float(split_packet[2])
    #print("X=", x ," Y=", y, " Z=", z)
    #print("X=", x)
    print(data_packet)
    count+=1
