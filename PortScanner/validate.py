import validators
import requests

def validate(ipOrUrl):
	toValidate = ipOrUrl
	str = "Valid Url"
	try:
		toValidate = "https://"+ipOrUrl
		requests = requests.get(toValidate, stream=True, timeout=3)
	except:
		try:
			toValidate = "http://"+ipOrUrl
			requests = requests.get(toValidate, stream=True, timeout=3)
		except:
			str="Error: Invalid hostname"
			if not(validators.ip_address.ipv4(ipOrUrl)):
				subIP = ipOrUrl.split(".")
				count = 0
				for i in subIP:
					if i.isdigit():
						count =+ 1
				if count == 4:
					str = "Error: Invalid IP address"
			else:
				str = "Valid IP"
	return str

