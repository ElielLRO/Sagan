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

aux = 0
tempos = []
tempo0 = 0
medida = 1
temp0 = []

def iniciar_tempo():
	tempo0 = time.time()
	temp0.append(tempo0)
	print "tempo iniciado\n"

def registrar_tempo():
	tempo = time.time()
	print "tempo %i coletado" % medida
	tot = tempo - temp0[0]
	tempos.append(tot)

def mostrar_tempos():
	aux = 1
	for i in tempos:
		print "t%i = %6.4f" %  (aux,i)
		aux += 1
	print "\n"

print("Pronto para a coleta de dados, pressione o botao para iniciar a contagem dos tempos")
while True:

	ser.write('B')	
	aux = ser.read(1)
	iniciar_tempo()
	for i in range(4):
		aux = ser.read(1)
		registrar_tempo()
		medida += 1
	mostrar_tempos()	
	tempos = []
	aux = 0
	medida = 1
	temp0 = []
	