#Shazna Khanom - Creation date: 14/04/21
from dynamixel_sdk import *     #imports all variables in Dynamixel SDK
from dxl_control.xl430_control_table import *

PROTOCOL_VERSION = 2.0
BAUDRATE = 57600
DEVICENAME ='COM6' #'/dev/ttyUSB0'
MIN_POS_VAL = 0
MAX_POS_VAL = 4095
DXL1_ID = 1
DXL2_ID = 2
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
groupBulkWrite = GroupBulkWrite(portHandler, packetHandler)
groupBulkRead = GroupBulkRead(portHandler, packetHandler)

class xl430:
    #function inside class
    def open_port():
        if portHandler.openPort():
            print("Successfully opened port")
        else:
            print("Failed to open port")
            print("Press any key to terminate...")
            quit()

    def set_baudrate():
        if portHandler.setBaudRate(BAUDRATE):
            print('Successfully changed the baud rate to {0} bps'.format(BAUDRATE))
        else:
            print('Failed to change baudrate')
            print("Press any key to terminate...")
            quit()

    def close_port():
        portHandler.closePort()
        print("Successfully closed port")

        ##Writes 1 byte
    def set_reg1(self, reg_num, reg_val):
        dxl_comm_result, dxl_error = xl430.packetHandler.write1ByteTxRx(portHandler, self.id, reg_num, reg_val)
        xl430.check_error(dxl_comm_result, dxl_error)

        ##Writes 2 bytes
    def set_reg2(self, reg_num, reg_val):
        dxl_comm_result, dxl_error = xl430.packetHandler.write2ByteTxRx(xl430.portHandler, self.id, reg_num, reg_val)
        xl430.check_error(dxl_comm_result, dxl_error)

        #reads 1 byte
    def get_reg1(self, reg_num):
        reg_data, dxl_comm_result,dxl_error = xl430.packetHandler.read1ByteTxRx(xl430.portHandler, self.id, reg_num)
        xl430.check_error(dxl_comm_result, dxl_error)
        return reg_data

        #reads 2 bytes
    def get_reg2(self, reg_num):
        reg_data, dxl_comm_result,dxl_error = xl430.packetHandler.read2ByteTxRx(xl430.portHandler, self.id, reg_num)
        xl430.check_error(dxl_comm_result, dxl_error)
        return reg_data

    def torque_enable(DXL_ID):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Torque Enabled: Dynamixel #%d has been successfully connected" % DXL_ID)


    def torque_disable(DXL_ID):
        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))
        else:
            print("Torque Disabled: Dynamixel #%d" % DXL_ID)

    def add_parameter(DXL_ID, ADDR, LEN_ADDR, PARAMETER):
        dxl_addparam_result = groupBulkWrite.addParam(DXL_ID, ADDR, LEN_ADDR, PARAMETER)
        if dxl_addparam_result!= True:
            print(print("[ID:%03d] groupBulkWrite addparam failed" % DXL_ID))
            quit()

    def bulk_write():
        dxl_comm_result = groupBulkWrite.txPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
