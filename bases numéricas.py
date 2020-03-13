while True:
	b = int(input('''Qual a base numérica que você deseja converter?
[ 1 ] para DECIMAL
[ 2 ] para BINARIO
[ 3 ] para OCTAL
[ 4 ] para HEXADECIMAL
Digite a opção desejada: '''))
	if b == 1:
		a = int(input('Digite o valor que será convertido: '))
		c = int(input('''Para qual base numérica você quer?
[ 1 ] para DECIMAL
[ 2 ] para BINARIO
[ 3 ] para OCTAL
[ 4 ] para HEXADECIMAL
Digite a opção desejada: '''))
		if c == 1:
			print('{} em DECIMAL é {}.'.format(a, a))
		elif c == 2:
			print('{} em BINARIO é {}.'.format(a, bin(a)[2:]))
		elif c == 3:
			print('{} em OCTAL é {}.'.format(a, oct(a)[2:]))
		elif c == 4:
			print('{} em HEXADECIMAL é {}.'.format(a, hex(a)[2:]))
		else:
			print('Opção invalida.')
			
	elif b == 2:
		print('Digite somente 0 e 1, pfv')
		a = int(input('Digite o valor que será convertido: '))
		dec = int(str(a), 2)
		c = int(input('''Para qual base numérica você quer?
[ 1 ] para DECIMAL
[ 2 ] para BINARIO
[ 3 ] para OCTAL
[ 4 ] para HEXADECIMAL
Digite a opção desejada: '''))
		if c == 1:
			print('{} em DECIMAL é {}.'.format(a, dec))
		elif c == 2:
			print('{} em BINARIO é {}.'.format(a, bin(dec)[2:]))
		elif c == 3:
			print('{} em OCTAL é {}.'.format(a, oct(dec)[2:]))
		elif c == 4:
			print('{} em HEXADECIMAL é {}.'.format(a, hex(dec)[2:]))
		else:
			print('Opção invalida.')
	elif b == 3:
		print('Digite somente do 0 ao 7, pfv')
		a = int(input('Digite o valor que será convertido: '))
		dec = int(str(a), 8)
		c = int(input('''Para qual base numérica você quer?
[ 1 ] para DECIMAL
[ 2 ] para BINARIO
[ 3 ] para OCTAL
[ 4 ] para HEXADECIMAL
Digite a opção desejada: '''))
		if c == 1:
			print('{} em DECIMAL é {}.'.format(a, dec))
		elif c == 2:
			print('{} em BINARIO é {}.'.format(a, bin(dec)[2:]))
		elif c == 3:
			print('{} em OCTAL é {}.'.format(a, oct(dec)[2:]))
		elif c == 4:
			print('{} em HEXADECIMAL é {}.'.format(a, hex(dec)[2:]))
		else:
			print('Opção invalida.')
	elif b == 4:
		a = input('Digite o valor que será convertido: ')
		dec = int(str(a), 16)
		c = int(input('''Para qual base numérica você quer?
[ 1 ] para DECIMAL
[ 2 ] para BINARIO
[ 3 ] para OCTAL
[ 4 ] para HEXADECIMAL
Digite a opção desejada: '''))
		if c == 1:
			print('{} em DECIMAL é {}.'.format(a, dec))
		elif c == 2:
			print('{} em BINARIO é {}.'.format(a, bin(dec)[2:]))
		elif c == 3:
			print('{} em OCTAL é {}.'.format(a, oct(dec)[2:]))
		elif c == 4:
			print('{} em HEXADECIMAL é {}.'.format(a, hex(dec)[2:]))
		else:
			print('Opção invalida.')
		
	continua = str(input('Deseja fazer outra converção? (S/N): '))
	if continua == 'N':
		break
	elif continua != 'S':
		print('opção invalida.')
		break