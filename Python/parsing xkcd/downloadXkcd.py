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
	print(res)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, "lxml")

	#Поиск URL-адреса изображения комикса.
	comicElem = soup.select('#comic img')
	print(comicElem)
	if comicElem == []:
		print('Не удалось найти изображение комикса.')
	else:
		comicUrl = comicElem[0].get('scr')
		#Загрузить изображение.
		print('Загружается изображение %s...' % (comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()

		#Сохранение ихображения в папке ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.
						basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	#Получение URL-адреса кнопки Prev.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')

print('Готово.')
