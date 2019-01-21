from Adafruit_CharLCD import Adafruit_CharLCD
from time import sleep
import Adafruit_DHT
import serial

SensorTemp = Adafruit_DHT.DHT11
PinSensorTemp = 18

Objlcd = Adafruit_CharLCD(rs=22, en=11, d4=23, d5=10, d6=9, d7=25, cols=16, lines=2)
ObjSerial = serial.Serial('/dev/ttyAMA0', 9600)
ObjSerial.close()
ObjSerial.open()

while True:
	ValueHumi, ValueTemp = Adafruit_DHT.read_retry(SensorTemp, PinSensorTemp)
	Objlcd.clear()

	if ValueHumi is not None and ValueTemp is not None:
		ObjString = 'Temp={0:0.1f}*C\nHumidity={1:0.1f}%\n'.format(ValueTemp, ValueHumi)
	else:
		ObjString = 'Failed to get Value\n'

	Objlcd.message(ObjString)
	ObjSerial.write(ObjString)
	sleep(1)
