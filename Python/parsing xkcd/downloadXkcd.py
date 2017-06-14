#! python3
# downloadXkcd.py - Загружает все комиксы XKCD.

import requests, os, bs4

url = 'http://xkcd.com' #начальный URL-адрес
os.makedirs('xkcd', exist_ok=True) 	# сохранияем комикс в
									# папке ./xkcd
while not url.endswith('#'):
	#Загрузка страницы.
	print('Загружается страница %s...' % url)
	res = requests.get(url)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text)

#TODO: URL-адрес изображения комикса.

#TODO: Загрузить изображение.

#TODO: Сохранить ихображение в папке ./xkcd.

#TODO: Получить URL-адрес кнопки Prev.

print('Готово.')
