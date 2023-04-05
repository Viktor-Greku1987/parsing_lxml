import requests
from bs4 import BeautifulSoup

link  = 'https://browser-info.ru/'
responce = requests.get(link).text
#print(responce)
soup = BeautifulSoup(responce, "lxml")
main = soup.find('div', id="main")
center = main.find('div', id="center")
tool = center.find('div', id="tool_padding")
ch_js = tool.find('div', id="javascript_check")
print(ch_js)


#check_js = block.find('div', id="javascript_check")
#print(check_js)