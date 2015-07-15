__author__ = 'Administrator'


class MusicItemModel(object):
	def __init__(self, name="", time="", popularity="", download_url=""):
		self.name_ = name
		self.time_ = time
		self.popularity_ = popularity
		self.download_url_ = download_url

	@property
	def name(self):
		return self.name_

	@name.setter
	def name(self, name):
		self.name_ = name

	@property
	def time(self):
		return self.time_

	@time.setter
	def time(self, time):
		self.time_ = time

	@property
	def popularity(self):
		return self.popularity_

	@popularity.setter
	def popularity(self, popularity):
		self.popularity_ = popularity

	@property
	def download_url(self):
		return self.download_url_

	@download_url.setter
	def download_url(self, download_url):
		self.download_url_ = download_url

	def save(self):
		pass

	def __repr__(self):
		return {"name": self.name_, "time": self.time_, "popularity": self.popularity_,
		        "download_url": self.download_url_}
