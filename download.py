from function import *

# def download(url, path):
# 	file = open(path, 'wb+')
# 	text = request_get(url).text
# 	print(text)
# 	file.write(text)
# 	file.close()

def download(url, path):
	print('wget -c "' + url + '" -O "' + path + '"')
	os.system('wget -c "' + url + '" -O "' + path + '"')