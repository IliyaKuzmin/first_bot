import requests
import json
from variables import headers
class Input_Error(Exception):
	pass
class convertor(object):
	def get_price(self,base,quote,amount):
		url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote}&from={base}&amount={amount}"

		payload = {}
		response = requests.request("GET", url, headers=headers, data = payload)

		status_code = response.status_code
		result = response.text
		TotalBase=json.loads(response.content)['result']
		return TotalBase 