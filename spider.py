import requests
import json as jsonlib
from function import *
from download import download

url_list = open('todo.txt', 'r+', encoding='utf8').read().split('\n')

def download_music(info, path):
	print('download music', path, info)
	cover_path = path + '.jpg'
	download(info['cover'], path + '.jpg')
	music_path = path + '.mp3'
	download(info['url_320'], path + '.mp3')

def download_page(url, path):
	text = request_post(url).text
	json = jsonlib.loads(text)['data']['list']
	page = '%02d' % int(url.split('page/')[1].split('/')[0])
	token = url.split('/')[-1]
	count = 0
	make_dir(path_join(os.getcwd(), 'download', '{page}@{token}'.format(page=page, token=token)))
	make_dir(path_join(path, dirname_formater.format(page=page, token=token)))
	for info in json:
		count = '%02d' % (int(count) + 1)
		full_info = dict(info, **{
			'page' : page,
			'token' : token,
			'count' : count,
			'count_plus': '%03d' % (20 * (int(page) - 1) + int(count)),
		})
		source_path = path_join(
			path_join(os.getcwd(), 'download'),
			'{page}@{token}'.format(page=page, token=token),
			'{token}#{count}'.format(token=token, count=count),
		)
		download_music(info, source_path)
		result_path = path_join(
			path,
			dirname_formater.format(**full_info),
			filename_formater.format(**full_info),
		)
		copy_file(source_path + '.mp3', result_path + '.mp3')

if __name__ == '__main__':
	for url in url_list:
		download_page(url, path_join(os.getcwd(), 'result'))