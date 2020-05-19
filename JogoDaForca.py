from random import choice

plv = ["carro", "casa", "cachorro", "capacete", "espelho", "porta", "cama", "cadeira", "chinelo", "quadro", "gato", "mesa", "fechadura", "toalha", "televisao", "paralelepipedo", "ventilador", "apaixonado", "desesperado", "varal", "cabide", "colher", "celular", "abajur", "caixa", "escova", "laranja", "sapato", "sabonete", "pente", "janela", "mochila", "mapa", "caminhao", "arroz", "cavalo", "grampeador", "camisa", "escritorio", "caderno", "biblioteca", "discoteca", "perfume", "desodorante", "livro"]

dicas = {"carro": "tem na garagem",
"casa": "tem onde vive pessoas",
"cachorro": "um animal",
"capacete": "segurança", 
"espelho": "tem no banheiro", 
"porta": "tem na casa", 
"cama": "tem no quarto", 
"cadeira": "serve para sentar", 
"chinelo": "pé", 
"quadro": "museu", 
"gato": "um animal", 
"mesa": "suporte", 
"fechadura": "porta", 
"toalha": "banho", 
"televisao": "aparelho eletrônico", "paralelepipedo": "rocha", 
"ventilador": "resfriamento de ambiente", "apaixonado": "emoção", 
"desesperado": "emoção", 
"varal": "roupa", 
"cabide": "roupa", 
"colher": "comida", 
"celular": "aparelho eletrônico", 
"abajur": "iluminação", 
"caixa": "guarda objetos", 
"escova": "higiene", 
"laranja": "cor", 
"sapato": "pé", 
"sabonete": "banho", 
"pente": "cabelo", 
"janela": "tem na casa", 
"mochila": "escola", 
"mapa": "caça ao tesouro", 
"caminhao": "veículo", 
"arroz": "comida", 
"cavalo": "um animal", 
"grampeador": "escritório", 
"camisa": "roupa", 
"escritorio": "trabalho", 
"caderno": "escola", 
"biblioteca": "livros", 
"discoteca": "diversão", 
"perfume": "cheiro", 
"desodorante": "cheiro", 
"livro": "escola"
}

sortear = choice(plv)
tentativas = 5
plv_esc = "_" * len(sortear)
plv_esc = list(plv_esc)

print("-=-" * 12)
print("JOGO DA FORCA".center(35))
print("-=-" * 12)

print(f"\nA dica é: \033[1;33m{dicas[sortear]}\033[m")

print(f"\n\033[1;34mVOCÊ TEM \033[1;33m{tentativas}\033[1;34m TENTATIVAS!\033[m\n")

letras_usadas = []

while True:
	print(" ".join(plv_esc))
	chute = input("\nDigite uma letra: ").lower()
	if chute in sortear:
		for num, c in enumerate(sortear):
			if chute == c:
				plv_esc[num] = sortear[num]
				
	else:
		tentativas -= 1
		print(f"\n\033[1;34mVOCÊ TEM \033[1;33m{tentativas}\033[1;34m TENTATIVAS!\033[m\n")
		
	if tentativas == 0:
		print("\nVocê perdeu...")
		print(f"A palavra era \033[1;33m{sortear}\033[m")
		break
		
	if "_" not in plv_esc:
		print(" ".join(plv_esc))
		print("\n\n\033[1;35mPARABENS, VOCÊ GANHOU!!!\033[m")
		break
		
	if chute in letras_usadas:
		print("\n\033[1;36mNÃO PODE USAR A MESMA LETRA MAIS DE UMA VEZ!!\033[m\n")
		
	letras_usadas.append(chute)