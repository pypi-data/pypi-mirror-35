import urllib.request

def check(string):
	url='http://safechat.tellter.com/check/'+string
	return urllib.request.urlopen(url).read().decode('utf-8')