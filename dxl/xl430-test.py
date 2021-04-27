from dxl_control.xl430 import *
import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

dxl_goal_position_1 = [MIN_POS_VAL, MAX_POS_VAL]
dxl_goal_position_2 = [MAX_POS_VAL, MIN_POS_VAL]
index = 0
DXL_MOVING_STATUS_THRESHOLD = 20

#DXL1_ID = 1
#DXL2_ID = 2
xl430.open_port()
xl430.set_baudrate()

#Enable Dynamixel #1 Torque
xl430.torque_enable(DXL1_ID)
#Enable Dynamixel #2 Torque
xl430.torque_enable(DXL2_ID)



groupBulkWrite.clearParam()

# Add parameter storage for Dynamixel#1 present position
dxl_addparam_result = groupBulkRead.addParam(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
if dxl_addparam_result != True:
    print("[ID:%03d] groupBulkRead addparam failed" % DXL1_ID)
    quit()

# Add parameter storage for Dynamixel#2 present position
dxl_addparam_result = groupBulkRead.addParam(DXL2_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
if dxl_addparam_result != True:
    print("[ID:%03d] groupBulkRead addparam failed" % DXL2_ID)
    quit()

while 1:
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(0x1b):
        break
    # Allocate goal position value into byte array
    param_goal_position_1 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_position_1[index])), DXL_HIBYTE(DXL_LOWORD(dxl_goal_position_1[index])), DXL_LOBYTE(DXL_HIWORD(dxl_goal_position_1[index])), DXL_HIBYTE(DXL_HIWORD(dxl_goal_position_1[index]))]
    param_goal_position_2 = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_position_2[index])), DXL_HIBYTE(DXL_LOWORD(dxl_goal_position_2[index])), DXL_LOBYTE(DXL_HIWORD(dxl_goal_position_2[index])), DXL_HIBYTE(DXL_HIWORD(dxl_goal_position_2[index]))]

    # Add Dynamixel#1 goal position value to the Bulkwrite parameter storage
    xl430.add_parameter(DXL1_ID, ADDR_GOAL_POSITION, LEN_GOAL_POSITION, param_goal_position_1)
    xl430.add_parameter(DXL2_ID, ADDR_GOAL_POSITION, LEN_GOAL_POSITION, param_goal_position_2)
    xl430.bulk_write()
    groupBulkWrite.clearParam()

    while 1:
        dxl_comm_result = groupBulkRead.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        # Check if groupbulkread data of Dynamixel#1 is available
        dxl_getdata_result = groupBulkRead.isAvailable(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        if dxl_getdata_result != True:
            print("[ID:%03d] groupBulkRead getdata failed" % DXL1_ID)
            quit()

        # Check if groupbulkread data of Dynamixel#2 is available
        dxl_getdata_result = groupBulkRead.isAvailable(DXL2_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        if dxl_getdata_result != True:
            print("[ID:%03d] groupBulkRead getdata failed" % DXL2_ID)
            quit()

         # Get present position value
        dxl1_present_position = groupBulkRead.getData(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        dxl2_present_position = groupBulkRead.getData(DXL2_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

        print("[ID:%03d] Present Position : %d \t [ID:%03d] Present Position: %d" % (DXL1_ID, dxl1_present_position, DXL2_ID, dxl2_present_position))

        if not (abs(dxl_goal_position_1[index] - dxl1_present_position) > DXL_MOVING_STATUS_THRESHOLD):
            break

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0


#Disable Dynamixel #1
xl430.torque_disable(DXL1_ID)
xl430.torque_disable(DXL2_ID)




#disconnect
xl430.close_port()
