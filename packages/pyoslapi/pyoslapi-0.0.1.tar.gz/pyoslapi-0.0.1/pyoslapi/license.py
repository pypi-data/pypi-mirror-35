# Copyright (c) 2018 Yuriy Lisovskiy
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://opensource.org/licenses/MIT

from .errors import TYPE_ERROR


# Represents downloaded license.
class License:

	def __init__(self, name, link, content):
		if not isinstance(name, str):
			raise TYPE_ERROR
		self.__name = name
		if not isinstance(link, str):
			raise TYPE_ERROR
		self.__link = link
		if not isinstance(content, str):
			raise TYPE_ERROR
		self.__content = content
	
	# Returns license full name.
	@property
	def name(self):
		return self.__name
	
	# Returns license source link.
	@property
	def link(self):
		return self.__link
	
	# Returns license content.
	@property
	def content(self):
		return self.__content
