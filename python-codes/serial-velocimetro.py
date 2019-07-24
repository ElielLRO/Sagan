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
time.sleep(2)

print("Digite o diametro da esfera(em centimetros)")
status = False

while status == False:
	diametro = raw_input()
	try:
		diametro = float(diametro)
		status = True
	except:
		if ',' in diametro:
			print("Use '.' ao inves de ','")
		else:
			print("Use apenas numeros")
print("Pronto para a coleta de dados.")

while True:
	ser.write('A')
	aux1 = ser.read(1)
	delt1 = time.time()
	aux1 = ser.read(1)
	delt2 = time.time()
	tempo = delt2-delt1
	velocidade = ((diametro/100.)/tempo)
	print tempo
