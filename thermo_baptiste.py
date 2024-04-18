from machine import Pin,ADC
from time import sleep_ms
from math import log

adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

ledr = Pin(5,Pin.OUT)
ledv = Pin(4,Pin.OUT)
ledb = Pin(2,Pin.OUT)

# t = 1 / (1/t1 + ln(Rt/R)/B)
# avec t la temperature actuelle

try:
    while True:
        adcValue = adc.read()
        U = adcValue/4095*3.3
        I = (3.3 - U)/10
        Rt = U/I
        t1 = 273.15 + 25
        R = 10
        B = 3950
        tempK = 1/ (1/t1 + log(Rt/R)/B)
        tempC = tempK - 273.15
        print("ADC value:",adcValue,"\tVoltage :",U,"\tTemperature :",tempC);
        if tempC > 25:
            ledr.value(1)
            ledv.value(0)
            ledb.value(0)
        elif tempC <= 25 and tempC > 23:
            ledr.value(0)
            ledv.value(1)
            ledb.value(0)
        else:
            ledr.value(0)
            ledv.value(0)
            ledb.value(1)
        sleep_ms(1000)
except:
    pass