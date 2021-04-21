#Shazna Khanom - Creation date: 14/04/2021 @11:45
#EEPROM Area control table
ADDR_MODEL_NUMBER = 0
ADDR_MODEL_INFORMATION = 2
ADDR_VERSION = 6
ADDR_ID = 7                         # Unique ID for each Dynamixel [0~253(0xFD)] - 254(0xFE) = Broadcast address to send instruction packet to all Dxl ID's
ADDR_BAUD_RATE = 8                  # Determines serial comm speed between controller and dynamixel
ADDR_RETURN_DELAY_TIME = 9          # If instrustion sent, status packet resurned after time of retrun delay time [0~254] - unit 2usec, e.g (10) = 20usec
ADDR_DRIVE_MODE = 10                # bit 2(0x04) - Profile config, 0 - Velocity based profile, 1 - time-based profile
                                    # bit 0(0x01) - Normal/Reverse Mode, 0 - Normal CCW(Positive), CW(Negative), 1 - Reverse
ADDR_OPERATING_MODE = 11            # 1 - Velocity Control, 3(Default) - Position control, 4 - Extended Pos control, 16 - PWM Control Mode
ADDR_SECONDARY_ID = 12              # Assigns secondary ID (0~252), not unique - used to group dynamixels to synchronise movement
ADDR_PROTOCOL_TYPE = 13
ADDR_HOMING_OFFSET = 20
ADDR_MOVING_THRESHOLD = 24          # Determines whether dxl is moving or not (0~1023) - when PRESENT_VELOCITY > moving threshold = moving(122) set to 1 otherwise 0
ADDR_TEMPERATURE_LIMIT = 31
ADDR_MAX_VOLTAGE_LIMIT = 32
ADDR_MIN_VOLTAGE_LIMIT = 34
ADDR_PWM_LIMIT = 36
ADDR_VELOCITY_LIMIT = 44
ADDR_MAX_POSITION_LIMIT = 48
ADDR_MIN_POSITION_LIMIT = 52
ADDR_SHUTDOWN = 63

#Control Table of RAM Area
ADDR_TORQUE_ENABLE = 64             # when set to 1 - Torque enabled and data in EEPROM locked
ADDR_LED = 65                       # flickers once when turned on
ADDR_STATUS_RETURN_LEVEL = 68       # decides how to return status packet, 0 - PING only, 1 - PING and READ, 2 - All instructions
ADDR_REGISTER_INSTRUCTIONS = 69
ADDR_HARDWARE_ERROR_STATUS = 70
ADDR_VELOCITY_I_GAIN = 76
ADDR_VELOCITY_P_GAIN = 78
ADDR_POSITION_D_GAIN = 80           # K_p*P         Position ctrl mode uses feedforward and PID gains
ADDR_POSITION_I_GAIN = 82           # K_p*I*(s)
ADDR_POSITION_P_GAIN = 84           # K_p*I/(s)
ADDR_FEEDFORWARD_SECOND_GAIN = 88   # K_FF2*(s^2)
ADDR_FEEDFORWARD_FIRST_GAIN = 90    # K_FF1*(s)
ADDR_BUS_WATCHDOG = 98
ADDR_GOAL_PWM = 100
ADDR_GOAL_VELOCITY = 104
ADDR_PROFILE_ACCELERATION = 108     # Vel-based profile - sets acceleration of profile, time-based - sets acceleration TIME of profile
ADDR_PROFILE_VELOCITY = 112         # Only used in position control mode, vel-based - sets max velocity, time-based - sets time span to reach velocity
ADDR_GOAL_POSITION = 116
ADDR_REALTIME_TICK = 120            # Unit - 1ms, Range - (0~32,767)
ADDR_MOVING = 122                   # Determines whether dxl is in motion or not
ADDR_MOVING_STATUS = 123            # Provides extra info about velocity profile, following error, profile ongoing, In-position
ADDR_PRESENT_PWM = 124
ADDR_PRESENT_LOAD = 126
ADDR_PRESENT_VELOCITY = 128
ADDR_PRESENT_POSITION = 132
ADDR_VELOCITY_TRAJECTORY = 136
ADDR_POSITION_TRAJECTORY = 140
ADDR_PRESENT_INPUT_VOLTAGE = 144
ADDR_PRESENT_TEMPERATURE = 146
#---INDIRECT ADDRESSES  1
ADDR_INDIRECT_ADDRESS_1 = 168
ADDR_INDIRECT_ADDRESS_2 = 170
ADDR_INDIRECT_ADDRESS_3 = 172
#.....
ADDR_INDIRECT_ADDRESS_27 = 220
ADDR_INDIRECT_ADDRESS_28 = 222
#---INDIRECT DATA 1
ADDR_INDIRECT_DATA_1 = 224
ADDR_INDIRECT_DATA_2 = 225
#.....
ADDR_INDIRECT_DATA_27 = 250
ADDR_INDIRECT_DATA_28 = 251
#---INDIRECT ADDRESSES 2
ADDR_INDIRECT_ADDRESS_29 = 758
ADDR_INDIRECT_ADDRESS_30 = 580
#.....
ADDR_INDIRECT_ADDRESS_55 = 630
ADDR_INDIRECT_ADDRESS_56 = 632
#---INDIRECT DATA 2
ADDR_INDIRECT_DATA_29 = 634
ADDR_INDIRECT_DATA_30 = 635
#.....
ADDR_INDIRECT_DATA_55 = 660
ADDR_INDIRECT_DATA_56 = 661

#--DATA BYTE LENGTHS
LEN_ID = 1
LEN_MOVING_THRESHOLD = 4
LEN_PRESENT_POSITION = 4
LEN_LED = 1
LEN_TORQUE_ENABLE = 1
LEN_GOAL_POSITION = 4
LEN_POSITION_P_GAIN = 2
LEN_POSITION_I_GAIN = 2
LEN_POSITION_D_GAIN = 2




#USER DEFINED
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
DYNAMIXEL_MOVING_STATUS_THRESHOLD = 20
