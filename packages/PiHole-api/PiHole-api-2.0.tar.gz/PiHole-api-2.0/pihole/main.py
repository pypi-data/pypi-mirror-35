import requests
import time
import hashlib

def inApiLink(ip, endpoint):
	return "http://"+ str(ip) +"/admin/scripts/pi-hole/php/"+ str(endpoint) +".php"

class Auth(object):
	def __init__(self, password):
		# PiHole's web token is just a double sha256 hash of the utf8 encoded password
		self.token = hashlib.sha256(hashlib.sha256(str(password).encode()).hexdigest().encode()).hexdigest()
		self.auth_timestamp = time.time()

class PiHole(object):
	# Takes in an ip address of a pihole server
	def __init__(self, ip_address):
		self.ip_address = ip_address
		self.auth_data = None
		self.refresh()
		self.pw = None
		
	
	def refresh(self):
		rawdata = requests.get("http://" + self.ip_address + "/admin/api.php?summary").json()
		
		if self.auth_data != None:
			topdevicedata = requests.get("http://" + self.ip_address + "/admin/api.php?getQuerySources=25&auth=" + self.auth_data.token).json()
			
			self.top_devices = topdevicedata["top_sources"]
			
			self.forward_destinations = requests.get("http://" + self.ip_address + "/admin/api.php?getForwardDestinations&auth=" + self.auth_data.token).json()
			
			self.query_types = requests.get("http://" + self.ip_address + "/admin/api.php?getQueryTypes&auth=" + self.auth_data.token).json()["querytypes"]
		
		# Data that is returned is now parsed into vars
		self.status = rawdata["status"]
		self.domain_count = rawdata["domains_being_blocked"]
		self.queries = rawdata["dns_queries_today"]
		self.blocked = rawdata["ads_blocked_today"]
		self.ads_percentage = rawdata["ads_percentage_today"]
		self.unique_domains = rawdata["unique_domains"]
		self.forwarded = rawdata["queries_forwarded"]
		self.cached = rawdata["queries_cached"]
		self.total_clients = rawdata["clients_ever_seen"]
		self.unique_clients = rawdata["unique_clients"]
		self.total_queries = rawdata["dns_queries_all_types"]
		self.gravity_last_updated = rawdata["gravity_last_updated"]
	
	def refreshTop(self, count):
		if self.auth_data == None:
			print("Unable to fetch top items. Please authenticate.")
			exit(1)
		
		rawdata = requests.get("http://" + self.ip_address + "/admin/api.php?topItems="+ str(count) +"&auth=" + self.auth_data.token).json()
		self.top_queries = rawdata["top_queries"]
		self.top_ads = rawdata["top_ads"]
		
	
	def getGraphData(self):
		rawdata = requests.get("http://" + self.ip_address + "/admin/api.php?overTimeData10mins").json()
		return {"domains":rawdata["domains_over_time"], "ads":rawdata["ads_over_time"]}
	
	def authenticate(self, password):
		self.auth_data = Auth(password)
		self.pw = password
		# print(self.auth_data.token)
	
	def getAllQueries(self):
		if self.auth_data == None:
			print("Unable to get queries. Please authenticate")
			exit(1)
		return requests.get("http://" + self.ip_address + "/admin/api.php?getAllQueries&auth=" + self.auth_data.token).json()["data"]
	
	def enable(self):
		if self.auth_data == None:
			print("Unable to enable pihole. Please authenticate")
			exit(1)
		requests.get("http://" + self.ip_address + "/admin/api.php?enable&auth=" + self.auth_data.token)
	
	def disable(self, seconds):
		if self.auth_data == None:
			print("Unable to disable pihole. Please authenticate")
			exit(1)
		requests.get("http://" + self.ip_address + "/admin/api.php?disable="+ str(seconds) +"&auth=" + self.auth_data.token)
	
	def getVersion(self):
		return requests.get("http://" + self.ip_address + "/admin/api.php?versions").json()
	
	def getDBfilesize(self):
		if self.auth_data == None:
			print("Please authenticate")
			exit(1)
		return float(requests.get("http://" + self.ip_address + "/admin/api_db.php?getDBfilesize&auth=" + self.auth_data.token).json()["filesize"])
	
	def getList(self, list):
		return requests.get(inApiLink(self.ip_address, "get") + "?list="+str(list)).json()
	
	def add(self, list, domain):
		if self.auth_data == None:
			print("Please authenticate")
			exit(1)
		with requests.session() as s:
			s.get("http://"+ str(self.ip_address) +"/admin/scripts/pi-hole/php/add.php")
			requests.post("http://"+ str(self.ip_address) +"/admin/scripts/pi-hole/php/add.php", data={"list":list, "domain":domain, "pw":self.pw}).text
			
	def sub(self, list, domain):
		if self.auth_data == None:
			print("Please authenticate")
			exit(1)
		with requests.session() as s:
			s.get("http://"+ str(self.ip_address) +"/admin/scripts/pi-hole/php/sub.php")
			requests.post("http://"+ str(self.ip_address) +"/admin/scripts/pi-hole/php/sub.php", data={"list":list, "domain":domain, "pw":self.pw}).text
