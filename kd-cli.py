def kusDili(tr:str):
	return tr.lower().replace('a', 'aga').replace('e', 'ege').replace('ı', 'ıgı').replace('i', 'igi').replace('u', 'ugu').replace('ü', 'ügü').replace('o', 'ogo').replace('ö', 'ögö').replace('â', 'âgâ').replace('ê', 'êgê').replace('î', 'îgî').replace('û', 'ûgû').replace('ô', 'ôgô')
def turkDili(kd:str):
	return kd.lower().replace('aga', 'a').replace('ege', 'e').replace('ıgı', 'ı').replace('igi', 'i').replace('ugu', 'u').replace('ügü', 'ü').replace('ogo', 'o').replace('ögö', 'ö').replace('âgâ', 'â').replace('êgê', 'ê').replace('îgî', 'î').replace('ûgû', 'û').replace('ôgô', 'ô')
print('Kuş Dili Çevirici v1.0')
print("Kuguş Digiligi Megetigin: " + kusDili(input("Türkçe Metin: ")))
print("Türkçe Metin: " + turkDili(input("Kuguş Digiligi Megetigin: ")))
