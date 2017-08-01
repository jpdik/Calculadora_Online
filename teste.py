data = {'valores': ['12', '+', '3']}

def calcular():
	l = data['valores']

	if l[0] == '+' or l[0] == '-':
		l.insert(0, "0.00")
	elif l[0] == '*' or l[0] == '/' or l[0] == '%':
		return None

	res = float(l[0])

	OPERATORS = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}

	def apply_operator(a, op, b):

	    method = '__%s__' % OPERATORS[op]
	    return getattr(float(b), method)(float(a))

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

	print res