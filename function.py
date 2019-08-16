import os
import requests

from os.path import join as path_join

dirname_formater = '{token}'
filename_formater = '{count_plus} - {name} - {artist}'

def make_dir(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

def request_get(url):
	while True:
		try:
			return requests.get(
				url,
				timeout = 1,
				headers = {
					'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_45_14) AppleWebKit/1145.14 (KHTML, like Gecko) Chrome/1145.1.4 Safari/1145.14',
				}
			)
		except:
			print('[warn] requests get error:', {'url': url})

def request_post(url):
	while True:
		try:
			return requests.post(
				url,
				timeout = 1,
				headers = {
					'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_45_14) AppleWebKit/1145.14 (KHTML, like Gecko) Chrome/1145.1.4 Safari/1145.14',
				}
			)
		except:
			print('[warn] requests post error:', {'url': url})

def merge_cover(cover, music):
	from mutagen.mp3 import MP3
	from mutagen.id3 import ID3, APIC, error
	audio = MP3(music, ID3=ID3)
	try:
		audio.add_tags()
	except error:
		pass
	audio.tags.add(
		APIC(
			encoding = 3,
			mime = 'image/png',
			type = 3,
			desc = u'Cover',
			data = open(cover, 'rb+').read()
		)
	)
	audio.save()

def copy_file(source_file, target_file):
	print('copy file', source_file, target_file)
	if os.path.exists(source_file) and not os.path.exists(target_file):
		os.system('cp "{s}" "{e}"'.format(
			s = source_file,
			e = target_file
		))