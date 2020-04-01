lista = open("dados/senhas.txt", "r")
lista = lista.readlines()
senha = str(input("Digite sua senha: "))
key = '085246'
contagem = 0
for linha in lista:
	linha = linha.rstrip()
	if senha == linha:
		print("Acesso liberado!")
		contagem = 1
	elif senha == key:
		ask1 = str(input("Deseja cadastrar uma nova senha? (S/N)"))
		if ask1 == 'S':
			ask2 = str(input("Digite a nova senha: "))
			if ask2 != key:
				cadastro = open("dados/senhas.txt", "r")
				conteudo = cadastro.readlines()
				conteudo.append("\n{}".format(ask2))
				cadastro = open("dados/senhas.txt", "w")
				cadastro.writelines(conteudo)
				cadastro.close()
				print("Senha cadastrada com sucesso!")
				contagem = 1
				break
if contagem != 1:
	exit()