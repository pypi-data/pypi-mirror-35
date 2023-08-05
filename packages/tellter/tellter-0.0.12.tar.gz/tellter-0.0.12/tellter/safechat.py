import urllib, urllib.request
doc='''
Pour faire une vérification Safechat, entrez 'safechat.check(string)'. Retourne 'True' si une vulgarité est détectée, 'False' dans le cas contraire.
'''

def check(string):
	url='http://api.safechat.tellter.com:9999/check/'+urllib.parse.quote(string)
	return urllib.request.urlopen(url).read().decode('utf-8')=='True'