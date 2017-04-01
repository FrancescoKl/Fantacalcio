import lxml.html
import urllib2
import pprint
#from openpyxl import load_workbook

team = {'P': ['VIVIANO', 'SKORUPSKI', 'KARNEZIS'], 'D': ['ACERBI', 'SILVESTRE', 'MASIELLO A', 'DE VRIJ', 'PALETTA', 'TOLOI', "DRAME'", 'RADU'], 'C': ['BRUNO FERNANDES', 'FREULER', 'CANDREVA', 'KURTIC', 'PELLEGRINI', 'PERISIC', 'JANKTO', 'BERTOLACCI'], 'A': ['ZAPATA D', 'SALAH', 'ICARDI', 'INSIGNE', 'MILIK', 'FARIAS']}

file = urllib2.urlopen('http://www.fantagazzetta.com/probabili-formazioni-serie-a')
data = file.read()
file.close()

doc = lxml.html.document_fromstring(data)
#wb = load_workbook(filename='Statistiche_Milano_Stagione_2016-17_Fantagazzetta.xlsx')

players1 = doc.xpath('//div[@class="tab-pane fade active in no-gutter"]/div/div[@class="row no-gutter"]/div[3]//div[@class="pname2 text-right"]/a/text()')
players2 = doc.xpath('//div[@class="tab-pane fade active in no-gutter"]/div/div[@class="row no-gutter"]/div[3]//div[@class="pname2 text-left"]/a/text()')
players3 = doc.xpath('//div[@class="tab-pane fade  in no-gutter"]/div/div[@class="row no-gutter"]/div[3]//div[@class="pname2 text-left"]/a/text()')
players4 = doc.xpath('//div[@class="tab-pane fade  in no-gutter"]/div/div[@class="row no-gutter"]/div[3]//div[@class="pname2 text-right"]/a/text()')

starters = players1 + players2 + players3 + players4

players1 = doc.xpath('//div[@class="tab-pane fade active in no-gutter"]/div/div[@class="row no-gutter"]/div[4]//div[@class="pname2 text-right"]/a/text()')
players2 = doc.xpath('//div[@class="tab-pane fade active in no-gutter"]/div/div[@class="row no-gutter"]/div[4]//div[@class="pname2 text-left"]/a/text()')
players3 = doc.xpath('//div[@class="tab-pane fade  in no-gutter"]/div/div[@class="row no-gutter"]/div[4]//div[@class="pname2 text-left"]/a/text()')
players4 = doc.xpath('//div[@class="tab-pane fade  in no-gutter"]/div/div[@class="row no-gutter"]/div[4]//div[@class="pname2 text-right"]/a/text()')

substitutes = players1 + players2 + players3 + players4

possible_lineup = {'starters': {'P': [], 'D': [], 'C': [], 'A': []}, 'substitutes': {'P': [], 'D': [], 'C': [], 'A': []}}

for key in team:
	for player in [i for i in team[key] if i in starters]:
		possible_lineup['starters'][key].append(player)

for key in team:
	for player in [i for i in team[key] if i in substitutes]:
		possible_lineup['substitutes'][key].append(player)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(possible_lineup)


