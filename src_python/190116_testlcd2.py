from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import Adafruit_DHT

SensorTemp = Adafruit_DHT.DHT11
PinSensorTemp = 18

Objlcd = Adafruit_CharLCD(rs=22, en=11, d4=23, d5=10, d6=9, d7=25, cols=16, lines=2)

while True:
	ValueHumi, ValueTemp = Adafruit_DHT.read_retry(SensorTemp, PinSensorTemp)
	Objlcd.clear()

	if ValueHumi is not None and ValueTemp is not None:
		ObjString = 'Temp={0:0.1f}*C \nHumidity={1:0.1f}%'.format(ValueTemp, ValueHumi)
	else:
		ObjString = 'Failed to get Value'

	Objlcd.message(ObjString)
	sleep(1)
