from connect import readValue , writeValue
from modbus.holding import read_holding
from modbus.input import read_input
from modbus.discrete import read_discrete
from modbus.coils import read_coils
from time import sleep

# writeValue("ReadRegisterType", "Holding")
# writeValue("ReadAddress", 4)
# writeValue("ReadCount", 4)
# writeValue("ReadUnit", 1)


while True:
    try:
        address = int(readValue("ReadAddress"))
        count = int(readValue("ReadCount"))
        unit = int(readValue("ReadUnit"))
        print(f"Reading with ACU {address} : {count} : {unit}") 
        registerType = readValue("RegisterType")
        if registerType == "Holding":
            print("Reading Holding")
            values = read_holding(addr=address , count=count , unit=unit)
        elif registerType == "input":
            print("Reading Input")
            values = read_input(addr=address , count=count , unit=unit)
        elif registerType == "discrete":
            values = read_discrete(addr=address , count=count , unit=unit)
        else:
            values = read_coils(addr=address , count=count , unit=unit)
        for i in range(0 , len(values)):
            pin = f"v{i+1}"
            value = values[i]
            writeValue(pin , value)
    except Exception as e:
        print(str(e))
    finally:
        sleep(3)