from modbus import client

def read_holding(addr = 1 , count = 2 , unit = 1):
    res = client.read_holding_registers(address=addr, count=count, unit=unit)  # for NSK temp scanner 
    
    if not res.isError():
        return res.registers
    else:
        raise Exception("Error while Reading Holding Registers")