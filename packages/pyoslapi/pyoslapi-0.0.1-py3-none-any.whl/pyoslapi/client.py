# Copyright (c) 2018 Yuriy Lisovskiy
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://opensource.org/licenses/MIT

from .consts import BASE_URL
from .license import License
from .errors import TYPE_ERROR
from .util import license_data, download_content


# Represents simple client for getting a license.
class Client:
	
	# Downloads the license from https://github.com/YuriyLisovskiy/licenses repository.
	@staticmethod
	def get_license(name):
		
		# Check if name is of type string.
		if not isinstance(name, str):
			raise TYPE_ERROR
		
		# Download license from https://github.com/YuriyLisovskiy/licenses/licenses.
		decoded_data = download_content(BASE_URL + '/licenses/' + name)
		if decoded_data is not None:
			
			# Get license name and source link by its keyword.
			l_name, l_link = license_data(name)
			return License(name=l_name, link=l_link, content=decoded_data.decode('utf-8'))
		return None
	
	# Downloads license header from https://github.com/YuriyLisovskiy/licenses repository.
	@staticmethod
	def get_header(name):
		
		# Check if name is of type string.
		if not isinstance(name, str):
			raise TYPE_ERROR
		
		# Download license from https://github.com/YuriyLisovskiy/licenses/licenses.
		data = download_content(BASE_URL + '/headers/' + name + '-header')
		if data is not None:
			return data.decode('utf-8')
		return None
	
	# Downloads list of available licenses from https://github.com/YuriyLisovskiy/licenses repository.
	@staticmethod
	def get_list():
		
		# Download license from https://github.com/YuriyLisovskiy/licenses/licenses.
		data = download_content(BASE_URL + '/' + 'LICENSE-LIST')
		if data is not None:
			return data.decode('utf-8')
