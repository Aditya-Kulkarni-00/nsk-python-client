from modbus import client

def read_input(addr = 1 , count = 4 , unit = 1):
    res = client.read_input_registers(address=addr , count=count , unit=unit)

    if not res.isError():
        return res.registers
    else:
        raise Exception("Error while Reading Input Registers")