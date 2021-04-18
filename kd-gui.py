from tkinter import *
def kusDili(tr:str):
	return tr.lower().replace('a', 'aga').replace('e', 'ege').replace('ı', 'ıgı').replace('i', 'igi').replace('u', 'ugu').replace('ü', 'ügü').replace('o', 'ogo').replace('ö', 'ögö').replace('â', 'âgâ').replace('ê', 'êgê').replace('î', 'îgî').replace('û', 'ûgû').replace('ô', 'ôgô')
def turkDili(kd:str):
	return kd.lower().replace('aga', 'a').replace('ege', 'e').replace('ıgı', 'ı').replace('igi', 'i').replace('ugu', 'u').replace('ügü', 'ü').replace('ogo', 'o').replace('ögö', 'ö').replace('âgâ', 'â').replace('êgê', 'ê').replace('îgî', 'î').replace('ûgû', 'û').replace('ôgô', 'ô')
pencere = Tk()
pencere.title('Kuguş Digiligi Çegevigirigicigi')
pencere.geometry('275x150')
pencere.resizable(0, 0)
baslik = Label(text='Kuş Dili Çevirici v1.0')
girdi = Entry()
cikti = Label(text='Çıktı')
def kodla():
	cikti['text'] = kusDili(girdi.get())
button = Button(
	text='Kodla!',
	command=kodla)
def coz():
	cikti['text'] = turkDili(girdi.get())
button1 = Button(
	text='Çöz!',
	command=coz)
def copy():
	pencere.clipboard_append(cikti['text'])
	pencere.update()
copy = Button(
	text='Kopyala!',
	command=copy)
baslik.pack()
girdi.pack()
cikti.pack()
button.pack()
button1.pack()
copy.pack()
pencere.mainloop()
