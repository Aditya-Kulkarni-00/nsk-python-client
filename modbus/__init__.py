from pymodbus.client.sync import ModbusSerialClient

# find tty port by comand dmesg | grep ttyUSB
# OR find tty port by comand dmesg | grep tty
# pip3 install  -U pymodbus


client = ModbusSerialClient(
    method='rtu',
    port='COM3',
    baudrate=9600,
    timeout=3,
    parity='N',
    stopbits=1,
    bytesize=8
)

if client.connect():  # Trying for connect to Modbus Server/Slave
    '''Reading from a  input register with the below content.'''
    #res = client.read_holding_registers(address=1, count=1, unit=1)
    print("Connected to client" )
    
else:
    print('Cannot connect to the Modbus Server/Slave')