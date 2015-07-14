import requests

def get_page_urls(count = -1):
	home_page = "http://sj.djyule.com/BD.asp?DJtype=jp"
	r = requests.get(home_page)
	
	#page = "http://sj.djyule.com/BD.asp?page=2&DJtype=jp"

