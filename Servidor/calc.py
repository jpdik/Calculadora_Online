#coding: utf-8

import socket

class Calc:
	def __init__(self, ip, porta):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.valores = ""
		self.result = ""

		try:
			self.socket.connect((ip, porta))
		except socket.error:
			print 'Não foi possivel instanciar a classe'

	def inserir_valores(self, valores):
		self.valores = valores

	def calcular(self):
		self.socket.send(self.valores)

		self.result = self.socket.recv(1024)

	def resultado(self):
		return self.result

	def close(self):
		self.socket.close()
