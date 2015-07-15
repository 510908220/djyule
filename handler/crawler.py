# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
from urlparse import urljoin
from multiprocessing import Process
from pymongo import MongoClient
import config


def _get(url):
	response = requests.get(url)
	if response.status_code == 200:
		# response.encoding = "gb2312"
		return response.content
	return ""


def _get_page_urls():
	page_urls = []
	home_page = "http://sj.djyule.com/BD.asp?DJtype=jp"
	html = _get(home_page)
	page_count = 0
	if html:
		soup = BeautifulSoup(html)
		div_page = soup.find('div', attrs={"class": "List_Page3"})
		if div_page:
			a_items = div_page.find_all("a")
			href = a_items[-1]["href"]
			page_count = int(href.split("=")[1].split("&")[0])

	for page_index in range(1, page_count + 1, 1):
		if page_index == 1:
			page_url = home_page
		else:
			page_url = "http://sj.djyule.com/BD.asp?page={page_index}&DJtype=jp".format(page_index=page_index)
		page_urls.append(page_url)
	return page_urls


def process_encode(func):
	def wrapper(*args, **kw):
		result = func(*args, **kw)
		result = result.encode("gbk", 'ignore')
		return result.decode("gbk")

	return wrapper


class MusicPage(object):
	def __init__(self, song_url):
		self.song_url_ = song_url
		self.html = _get(song_url)
		self.soup = BeautifulSoup(self.html)

	@property
	@process_encode
	def song_url(self):
		return self.song_url_

	@property
	@process_encode
	def name(self):
		title = self.soup.title.string
		if not title:
			title = ""
		return title

	@property
	@process_encode
	def time(self):
		div_list = self.soup.find('div', attrs={"class": "downList"})
		item_li = div_list.find_all("li")[0]
		return item_li.text

	@property
	@process_encode
	def popularity(self):
		div_list = self.soup.find('div', attrs={"class": "downList"})
		item_li = div_list.find_all("li")[1]
		return item_li.text

	@property
	@process_encode
	def download_url(self):
		div_player = self.soup.find('div', attrs={"class": "playerDJ"})
		text = div_player.text
		return re.findall("<source src='(.*?)'", text)[0]


class MusicCrawler(object):
	def __init__(self):
		#Process.__init__(self)
		self.page_urls = _get_page_urls()
		self.client = MongoClient('mongodb://localhost:27017/')
		self.tb = self.client[config.DB_NAME][config.TB_MUSIC]

	@staticmethod
	def _parse(content):
		song_urls = []
		soup = BeautifulSoup(content)
		div_list = soup.find('div', attrs={"class": "List30"})
		li_items = div_list.find_all('a')
		for li_item in li_items:
			song_urls.append(urljoin(config.BASE_URL, li_item['href']))
		return song_urls

	def process_page(self, page_url):
		content = _get(page_url)
		if content:
			song_urls = MusicCrawler._parse(content)
			for song_url in song_urls[:2]:
				music_page = MusicPage(song_url)
				if music_page.name:
					record = {
						"name": music_page.name,
						"time": music_page.time,
						"popularity": music_page.popularity,
						"download_url": music_page.download_url
					}
					self.tb.insert_one(record)


	def run(self):
		for page_url in self.page_urls:
			self.process_page(page_url)


if __name__ == "__main__":
	process = MusicCrawler()
	# process.daemon = True  # 守护进程
	process.run()
