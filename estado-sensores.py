import serial,commands
from sys import stdout
from time import sleep
status = False 

while status == False:
	OUTPUT = commands.getoutput("python -m serial.tools.list_ports")
	if OUTPUT == 'no ports found':
		print("Arduino nao encontrado, conecte o arduino ao computadpr e tente novamente")
		while 1:pass
	else: status = True 

OUTPUT = OUTPUT.split()

for i in OUTPUT:
	if i.find("/dev/ttyACM") == 0:
		print("Arduino encontrado em %s") % i
		URL = i

ser = serial.Serial(URL, baudrate = 14400, timeout = None)
sleep(2)

print('Botao:       Sensor: ')
while True:
	ser.write('s')
	aux = ser.readline()
	ESTADO_SENSOR = str(int(aux) == 1)
	ser.write('b')
	aux = ser.readline()
	ESTADO_BOTAO = str(int(aux) == 1)
	if type(ESTADO_BOTAO) and type(ESTADO_SENSOR) == str:
		stdout.write(("\r%s         %s")%(ESTADO_BOTAO,ESTADO_SENSOR))
		stdout.flush()
		stdout.write("           ")
		stdout.flush()