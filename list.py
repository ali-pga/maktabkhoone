import 	requests
from bs4 import BeautifulSoup
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url',help='url')
parser.add_argument('-s','--size',help='size',type=int,default='0')
parser.add_argument('low', help = 'quality', default='high')
parser.add_argument('-d' , '--destination' , help='destination file address' , default='link.txt')
args=parser.parse_args()

linkpage=open(args.destination,'w')

for n in range(1,(args.size+1)):
	page = requests.get(args.url+str(n))
	soup = BeautifulSoup(page.content,'html.parser')
	if(args.low=='low'):
		link = soup.find('a','video-dl')
	else:
		link=soup.find('a','hq-video-dl')
	linkpage.write(str(link['href'])+"\n")

linkpage.close()

#while read url; do axel $url; done < mylinks.txt
