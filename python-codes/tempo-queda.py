import serial, commands, time

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
time.sleep(2.5)
print("Pronto para a coleta de dados.")
while True:

	ser.write('D')
	aux1 = ser.read(1)
	delt1 = time.time()
	aux1 = ser.read(1)
	delt2 = time.time()
	tempo = delt2-delt1
	print tempo