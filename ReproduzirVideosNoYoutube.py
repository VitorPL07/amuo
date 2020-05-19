from youtube_search import YoutubeSearch
import webbrowser as web

pg = input("Digite sua pesquisa: ")

nome = []
links = []
identificacao = []

pesquisa = YoutubeSearch(pg, max_results=4).to_dict()

for c in pesquisa:
	nome.append(c["title"])
	links.append(c["link"])
	
for i in range(len(nome)):
	identificacao.append(i + 1)
print("CÓDIGO    //    TITULO")
for a in range(len(nome)):
	print(f"\n[ \033[1;34m{identificacao[a]}\033[m ] - {nome[a]}")

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
