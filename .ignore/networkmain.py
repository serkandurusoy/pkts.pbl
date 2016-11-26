import machine
import time

#Digits and GPIO mappings
setD0 = machine.Pin(14,machine.Pin.OUT)
setD1 = machine.Pin(12,machine.Pin.OUT)
setD2 = machine.Pin(13,machine.Pin.OUT)
setD3 = machine.Pin(03,machine.Pin.OUT)

setD0.high()
setD1.high()
setD2.high()
setD3.high()

#Segments and 8Bit mappings
d0 = b'\357'
d1 = b'\44'
d2 = b'\325'
d3 = b'\165'
d4 = b'\66'
d5 = b'\163'
d6 = b'\363'
d7 = b'\45'
d8 = b'\377'
d9 = b'\67'

#Operational lists
segments = [d0,d1,d2,d3,d4,d5,d6,d7,d8,d9]
digits = [setD0,setD1,setD2,setD3]

#Define I2C
i2c = machine.I2C(machine.Pin(5), machine.Pin(4))

#Test Loop
for digitIndex in range(0,4):
    digits[digitIndex].low()
    for segmentIndex in range(0,9):
        i2c.writeto(39,segments[segmentIndex])
        time.sleep(0.5)
    pass
    digits[digitIndex].high()

#Fix 0 to screen
while True:
    for digitIndex in range(0,4):
        digits[digitIndex].low()    #Set Digit ON
        if digitIndex == 0:
            i2c.writeto(39,d3)          #Print 0 to Digit
            pass
        if digitIndex == 1:
            i2c.writeto(39,d2)          #Print 0 to Digit
            pass
        if digitIndex is 2:
            i2c.writeto(39,d1)          #Print 0 to Digit
            pass
        if digitIndex is 3:
            i2c.writeto(39,d0)          #Print 0 to Digit
            pass
        time.sleep(0.0025)
        digits[digitIndex].high()   #Set Digit OFF
        time.sleep(0.0025)
        pass
    pass
