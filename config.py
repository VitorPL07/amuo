import requests as rq
import webbrowser as web

version = "1.2"
cidade = 'piripiri'

def intro():
	msg = "Assistente - version {} / criador: VitorPL".format(version)
	print("~" * len(msg) +  "\n{}\n".format(msg)  +   "~" * len(msg))

lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]

conversas = {
	"oi": "Olá, tudo bem?",
	"sim e você": "Estou bem obrigada por perguntar"
}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}

def calcula(entrada):
	if "mais" in entrada or "+" in entrada:
		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) + int(entradas_recebidas[3])
	elif "menos" in entrada or "-" in entrada:
		entradas_recebidas = entrada.split(" ")
		resultado = int(entradas_recebidas[1]) - int(entradas_recebidas[3])
	elif "vezes" in entrada or "x" in entrada:
		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) * float(entradas_recebidas[3]), 2)
	elif "dividido" in entrada or "/" in entrada:
		entradas_recebidas = entrada.split(" ")
		resultado = round(float(entradas_recebidas[1]) / float(entradas_recebidas[4]), 2)
	else:
		resultado = "Operação não encontrada"

	return resultado

def clima_tempo():	
	endereco_api = "http://api.openweathermap.org/data/2.5/weather?appid=9e1280f88eef9db700e867bb898fd3ec&q="
	url = endereco_api + cidade

	infos = rq.get(url).json()

	# Coord
	longitude = infos['coord']['lon']
	latitude = infos['coord']['lat']
	# main
	temp = infos['main']['temp'] - 273.15 # Kelvin para Celsius
	pressao = infos['main']['pressure'] / 1013.25 #Libras para ATM
	humidade = infos['main']['humidity'] # Recebe em porcentagem
	temp_max= infos['main']['temp_max'] - 273.15 # Kelvin para Celsius
	temp_min = infos['main']['temp_min'] - 273.15 # Kelvin para Celsius

	#vento
	v_speed = infos['wind']['speed'] # km/ h
	v_direc = infos['wind']['deg'] #Recebe em graus

	#clouds / nuvens
	nebulosidade = infos['clouds']['all']

	#id
	id_da_cidade = infos['id']

	# 11
	return [longitude, latitude, 
		temp, pressao, humidade, 
		temp_max, temp_min, v_speed, 
		v_direc, nebulosidade, id_da_cidade]

def temperatura():
	temp_atual = clima_tempo()[2]
	temp_max = clima_tempo()[5]
	temp_min = clima_tempo()[6]
	
	return [temp_atual, temp_max, temp_min]

def abrir(fala):
	try:
		if "google" in fala:
			web.get(caminho_navegador).open("google.com.br/")
			return "abrindo google"
		elif "facebook" in fala:
			web.get(caminho_navegador).open("facebook.com.br/")
			return "abrindo facebook"
		else:
			return "site não cadastrado para aberturas"
	except:
		return "houve um erro"