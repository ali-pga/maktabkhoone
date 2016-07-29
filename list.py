import 	requests
from bs4 import BeautifulSoup
import sys
linkpage=open('link.txt','w')
for n in range(1,21):
	page = requests.get('http://maktabkhooneh.org/video/soleimani-ai-'+str(n))
	soup = BeautifulSoup(page.content,'html.parser')
	link = soup.find('a','hq-video-dl')
	linkpage.write(str(n)+'.'+str(link['href'])+"\n")
linkpage.close()

