from tkinter import *

class Janela:
	def __init__(self, master=None):
		self.fonte = ("Arial", "12", "bold")
		self.titulo = Label(master, text="Digite um texto", font=self.fonte)
		self.titulo.pack()
		master.geometry("400x250")
		self.retorno1 = Label(master, text="", font=self.fonte)
		self.retorno1.place(x=170, y=170)
		self.retorno2 = Label(master, text="", font=self.fonte)
		self.retorno2.place(x=170, y=200)

		self.entrada = Entry(master, width=30)
		self.entrada.place(x=105, y=40)

		self.botao = Button(master, text="Ok", font=self.fonte, width=15, command=self.Codificar)
		self.botao.place(x=120, y=100)

	def Codificar(self):
		letras = list(self.entrada.get())
		resultado = list()
		for letra in letras:
		    ascii = ord(letra)
		    novoascii = ascii + 5
		    novaletra = chr(novoascii)
		    resultado.append(novaletra)

		final = ''.join(resultado)
		self.retorno1["text"] = final

		desc = list(final)
		res = list()
		for descl in desc:
		    ascii = ord(descl)
		    novoascii = ascii - 5
		    novaletra = chr(novoascii)
		    res.append(novaletra)

		finaldesc = ''.join(res)

		self.retorno2["text"] = finaldesc

root = Tk()
Janela(root)
root.mainloop()