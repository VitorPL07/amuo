from youtube_search import YoutubeSearch
import webbrowser as web

# Pegar a pesquisa desejada
pg = input("Digite sua pesquisa: ")

# Criar listas para armazenar os dados de casa resultado
nome = []
links = []
identificacao = []

# Rodas a lib com a pesquisa digitada
pesquisa = YoutubeSearch(pg, max_results=4).to_dict()

# Armazenar os resultados da pesquisa nas listas correspondentes
for c in pesquisa:
	nome.append(c["title"])
	links.append(c["link"])
	
# Colocar uma maneira de escolher qual vídeo deseja ser aberto
for i in range(len(nome)):
	identificacao.append(i + 1)

# Apresentar os resultados de maneira intuitiva
print("CÓDIGO    //    TITULO")
for a in range(len(nome)):
	print(f"\n[ \033[1;34m{identificacao[a]}\033[m ] - {nome[a]}")

# Criar um loop e só quebrar caso o usuário escolha uma opção válida
while True:
	try:
		abrir = int(input("\nDigite o código referente ao vídeo que deseja abrir: "))
		if 0 < abrir < 5:
			you = ("https://www.youtube.com/")
			tube = links[abrir - 1]
			web.open(you + tube)
			break
		else:
			print("Opção inválida.")
	except:
		print("Opção inválida.")
