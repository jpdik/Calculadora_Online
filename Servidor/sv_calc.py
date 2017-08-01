#coding: utf-8

import socket
from hashlib import md5
import time
import os
import sys
import json

def calculadora(l = []):
	if l[0] == '+' or l[0] == '-':
		l.insert(0, "0.00")
	elif l[0] == '*' or l[0] == '/' or l[0] == '%':
		return None

	OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}

	def apply_operator(a, op, b):

	    method = '__%s__' % OPERATORS[op]
	    return getattr(float(b), method)(float(a))

	try:
		i = 0

		while i < len(l):
			if l[i] == '*' or l[i] == '/':
				l[i] = apply_operator(l[i+1], l[i], l[i-1])
				del l[i+1]
				del l[i-1]
				i -= 1
			else:
				i += 1

		i = 0

		while i < len(l):
			if l[i] == '+' or l[i] == '-':
				l[i] = apply_operator(l[i+1], l[i], l[i-1])
				del l[i+1]
				del l[i-1]
				i = 0
			else:
				i += 1

		return l[0]
	except ValueError:
		return None
	except ZeroDivisionError:
		return None

while True:
	#Cria  objeto socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#O argumento é uma tupla de 2 posições
	s.bind(('127.0.0.1', 8888))

	#Coloca o socket pra aguardar conexões, trava nessa parte
	s.listen(1)

	#Interrompe o fluxo de execução do programa, usa 2 variaveis pra pegar os 2 valores da tupla
	con, info_cli = s.accept()
	print 'Conexão estabelecida por', info_cli

	while True:
		dados = con.recv(1024)

		if not dados:
			break

		d = json.loads(dados)

		res = calculadora(d['valores'])

		print res

		if res == None:
			dados = json.dumps({'Erro': True, 'Resultado' : ''})
		else:
			dados = json.dumps({'Erro': False, 'Resultado' : str(res)})

		con.send(dados)

	con.close()