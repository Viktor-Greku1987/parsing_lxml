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

off  = ch_js.find_all('span')[1].text
result_js = f'javascript: {off}'
print('off = ', result_js)
print(result_js)


div_flash = tool.find('div', id="flash_version")
#div_user = tool.find('div', id="user_agent" )
#user_ag = div_user.find_all('span', attrs= {"class":"option_title"})

flash = div_flash.find_all('span')[1].text
result_flash = f'flash: {flash}'

check_user = tool.find('div', id = "user_agent").text
print("check_user: = ", check_user)

