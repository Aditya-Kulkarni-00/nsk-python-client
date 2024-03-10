from modbus import client

def read_coils(addr = 1 , count = 2 , unit = 1):
    res = client.read_coils(address=addr, count=count, unit=unit)  # for NSK temp scanner 
    
    if not res.isError():
        return res.registers
    else:
        raise Exception("Error while Reading Coil Registers")