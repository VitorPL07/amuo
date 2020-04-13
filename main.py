import speech_recognition as sr
import pyttsx3
from config import *
from random import choice

en = pyttsx3.init()
voices = en.getProperty('voices')
en.setProperty('rate', 175)
for voice in voices:
    if voice.languages[0] == b'\x05pt-br':
        en.setProperty('voice', voice.id)
        break

def sai_som(reposta):
    en.say(reposta)
    en.runAndWait()

user = "Bem vindo Vitor"

def assistente():
    print("=" * len(user))
    print(user)
    print("=" * len(user))
    sai_som(user)
    print("Ouvindo...")

    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        # rec = sr.Recognizer()

        # with sr.Microphone() as s:
        # rec.adjust_for_ambient_noise(s)

        while True:
            try:
                # audio = rec.listen(s)
                entrada = input("")
                entrada = entrada.lower()
                print("User: {}".format(entrada.capitalize()))

                # Abri links no navegador
                if "abrir" in entrada:
                    reposta = abrir(entrada)

                # Operações matemáticas
                elif "quanto é" in entrada:
                    entrada = entrada.replace("quanto é", "")
                    reposta = calcula(entrada)
                # Pede tempo
                elif "qual a temperatura" in entrada:

                    lista_tempo = temperatura()
                    temp = lista_tempo[0]
                    temp_max = lista_tempo[1]
                    temp_min = lista_tempo[2]

                    reposta = "A temperatura de hoje é {:.2f}º. Temos uma máxima de {:.2f}º e uma minima de {:.2f}º".format(
                        temp, temp_max, temp_min)

                # Informações da cidade
                elif "informações" in entrada and "cidade" in entrada:

                    reposta = "Mostrando informações da cidade"
                else:
                    reposta = conversas[entrada]

                if reposta == "Mostrando informações da cidade":
                    # mostra informações da cidade

                    lista_infos = clima_tempo()
                    longitude = lista_infos[0]
                    latitude = lista_infos[1]
                    temp = lista_infos[2]
                    pressao = lista_infos[3]
                    humidade = lista_infos[4]
                    temp_max = lista_infos[5]
                    temp_min = lista_infos[6]
                    v_speed = lista_infos[7]
                    v_direc = lista_infos[8]
                    nebulosidade = lista_infos[9]
                    id_da_cidade = lista_infos[10]

                    print("Assistente:")
                    print("Mostrando informações de {}\n\n".format(cidade))
                    sai_som("Mostrando informações de {}".format(cidade))
                    print("Longitude: {}, Latitude: {}\nId: {}\n".format(longitude, latitude, id_da_cidade))
                    print("Temperatura: {:.2f}º".format(temp))
                    print("Temperatura máxima: {:.2f}º".format(temp_max))
                    print("Temperatura minima: {:.2f}º".format(temp_min))
                    print("Humidade: {}".format(humidade))
                    print("Nebulosidade: {}".format(nebulosidade))
                    print("Pressao atmosférica: {}".format(pressao))
                    print("Velocidade do vento: {}m/s\nDireção do vento: {}".format(v_speed, v_direc))

                else:
                    print("Assistente: {}".format(reposta))
                    sai_som("{}".format(reposta))

            except sr.UnknownValueError:
                sai_som(resposta_erro_aleatoria)
            except KeyError:
                pass


if __name__ == '__main__':
    intro()
    sai_som("Iniciando")
    assistente()