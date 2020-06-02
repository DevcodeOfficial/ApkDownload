import requests, webbrowser
from bs4 import BeautifulSoup

def dl(app_name, path):
	res = requests.get(f"https://m.apkpure.com/search?q={app_name}")
	soup = BeautifulSoup(res.text, 'html.parser')
	result = soup.select('.dd')
	for link in result[:1]:
		s_for_name = requests.get("https://m.apkpure.com" + link.get('href'))
		sfn = BeautifulSoup(s_for_name.text, 'html.parser')
		ttl = sfn.select_one('title').text
		noneed = [' - APK Download']
		for i in noneed:
			name = ttl.replace(i, '')
			res2 = requests.get("https://m.apkpure.com" + link.get('href') + "/download?from=details")
			soup2 = BeautifulSoup(res2.text, 'html.parser')
			result = soup2.select('.ga')
		for link in result:
			dl_link = link.get('href')
			r = requests.get(dl_link) 
			with open(f"{path}/{name} www.technoayan.com .apk", 'wb') as f:
				f.write(r.content)
				print(f"{name} Downloaded Successfully")
