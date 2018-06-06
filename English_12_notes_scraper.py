from bs4 import BeautifulSoup
import requests
from fpdf import FPDF

res = requests.get("http://www.learncbse.in/chapter-wise-important-questions-class-12-english/")

soup1 = BeautifulSoup(res.text, 'lxml')

list_of_links = []

sample_str= 'http://www.cbsesamplepapers.info/cbse/'

for link in soup1.findAll('a'):

	if(type(link.get('href'))==str):
		if(sample_str in link.get('href')):
			list_of_links.append(link.get('href'))
		 


print(len(list_of_links))


for urls in list_of_links:
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('Arial','', 12)

	res = requests.get(urls)

	soup = BeautifulSoup(res.text, 'lxml')
	name = soup.title.text
	pdf.set_title(name)

	divObj = soup.find('div', {'class': 'entry-content'})
	qa_container = divObj.find_all('p');
	

	for qa in qa_container:

		excess = qa.find('a')

		if(excess):
			continue
		else:
			#pdf.cell(10,5,name)
			text = qa.text.encode('latin-1', 'ignore').decode('latin-1')
			pdf.multi_cell(0,5, text)
			pdf.ln()

	pdf.output(name+'.pdf').encode('latin-1')
	pdf.close()