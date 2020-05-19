alf = "abcdefghijklmnopqrstuvwxyz"

# Letras maiusculas e minusculas em listas
alf_min = list(alf)
alf_M = alf.upper()
alf_M = list(alf_M)
		
# Perguntar a senha
senha = str(input("Digite sua senha: "))

# Pegar a quantidade de letras
senha_quant = len(senha)


# Descobrir a senha
if senha_quant == 1:
	for c in alf_min:
		print(c)
		if c == senha:
			print("Pronto")
			exit()
	for b in alf_min:
		print(b)
		if b == senha:
			print("Pronto")
			exit()

elif senha_quant == 2:
	for c in alf_min:
		for b in alf_min:
			y = c + b
			print(y)
			if y == senha:
				print("Pronto")
				exit()
	for b in alf_M:
		for c in alf_M:
			y = b + c
			print(y)
			if y == senha:
				print("Pronto")
				exit()

elif senha_quant == 3:
	for c in alf_min:
		for b in alf_min:
			for a in alf_min:
				y = c + b + a
				print(y)
				if y == senha:
					print("Pronto")
					exit()
	for b in alf_M:
		for c in alf_M:
			for a in alf_M:
				y = b + c + a
				print(y)
				if y == senha:
					print("Pronto")
					exit()

elif senha_quant == 4:
	for c in alf_min:
		for b in alf_min:
			for a in alf_min:
				for d in alf_min:
					y = c + b + a + d
					print(y)
					if y == senha:
						print("Pronto")
						exit()
	for b in alf_M:
		for c in alf_M:
			for a in alf_M:
				for d in alf_M:
					y = b + c + a + d
					print(y)
					if y == senha:
						print("Pronto")
						exit()
