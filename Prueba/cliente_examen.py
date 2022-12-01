import threading
import sys
import socket
import pickle
import os
class Cliente():

	def __init__(self, host=input("Intoduzca la IP del servidor ?  "), port=int(input("Intoduzca el PUERTO del servidor ?  ")), nickname=input("Intoduzca su NICKNAME  ")): #constructor de cliente
		self.s = socket.socket()
		self.s.connect((host, int(port)))
		self.enviar('$'+nickname)
		print('\n\tProceso con PID = ',os.getpid(), '\n\tHilo PRINCIPAL con ID =',threading.currentThread().getName(), '\n\tHilo en modo DAEMON = ', threading.currentThread().isDaemon(),'\n\tTotal Hilos activos en este punto del programa =', threading.active_count())
		threading.Thread(target=self.recibir, daemon=True).start()

		while True:
			msg = input('\nEscriba texto ?   ** Enviar = ENTER   ** Salir Chat = 1 \n')
			if msg != '1' : self.enviar(msg)
			else:
				print("", os.getpid())
				self.s.close()
				sys.exit()

	def recibir(self):
		print('\nHilo RECIBIR con ID =',threading.currentThread().getName(), '\n\tPertenece al PROCESO con PID', os.getpid(), "\n\tHilos activos TOTALES ", threading.active_count())
		while True:
			try:
				data = self.s.recv(32)
				if data: print(pickle.loads(data))
			except: pass

	def enviar(self, msg):
		self.s.send(pickle.dumps(msg))

arrancar = Cliente()
