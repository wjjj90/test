import serial
serBarCode = serial.Serial('COM19', 115200, timeout=1)
while True:

    #read data from serial port
    data = serBarCode.readline()

    #if there is smth do smth
    if len(data) >= 1:
        print(data.decode("utf-8"))
        
        
        
        
        
        cycccccc
