'''
A Tellter project
TellterNeuralSystem (TNS) - Public / Open source API
Tellter 2018. MIT license.
'''
import urllib.request

class ServerAPI:
	def __init__(self):
		with open("reports/list.json") as self.reports_list_file:
			self.reports_list=self.reports_list_file.read().split(" ")
		self.reports_list_file.close()
	def fetch(self, url):
		return urllib.request.urlopen(url).read().decode('utf-8')
	def request_trigger(self, message):
		message=message.replace(" ","%20")
		self.url='http://api.tns.tellter.com:5000/trigger/'+message
		return self.fetch(self.url)
	def request_convert(self, triggered_item):
		self.url='http://api.tns.tellter.com:5000/conversion/'+triggered_item
		return self.fetch(self.url)

class DataManager:
	def refresh_reports(self):
		with open("reports/list.json") as self.reports_list_file:
			self.reports_list=self.reports_list_file.read().split(" ")
		self.reports_list_file.close()
	def initialize(self, username):
		self.timestamp=urllib.request.urlopen('http://api.tns.tellter.com:5000/uniqueid').read().decode('utf-8')
		self.report_name=username+"_"+self.timestamp
		self.path="reports/"+self.report_name+".txt"
		self.report_file=open(self.path,"w+")
		print(self.report_name)
		self.report_file.close()

		self.reports_list.append(self.report_name)
		with open("reports/list.json","w") as reports_list_modification:
			reports_list_modification.write(" ".join(self.reports_list))
		self.refresh_reports()


	def is_user_reported(self, username):
		self.refresh_reports()
		if username in "".join(self.reports_list):
			for report in self.reports_list:
				if username in report:
					return (True, report)

		else:
			return (False, 0)
			

	def write(self, username, converted_data): # Write extracted data into user's report
		# Finding user's report
		self.is_reported=self.is_user_reported(username)
		if self.is_reported[0]:
			self.user_report="reports/"+self.is_reported[1]+".txt"
		else:
			self.initialize(username)
			self.user_report="reports/"+self.is_user_reported(username)[1]+".txt"
		# Writing
		with open(self.user_report,"a") as user_report_file:
			for element in converted_data:
				user_report_file.write(element)
