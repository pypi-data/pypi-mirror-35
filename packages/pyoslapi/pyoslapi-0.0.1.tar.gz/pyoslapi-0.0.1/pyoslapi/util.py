# Copyright (c) 2018 Yuriy Lisovskiy
# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://opensource.org/licenses/MIT

import json
import base64
import requests

from .consts import GNU_ORG, OPEN_SOURCE_ORG
from .errors import TYPE_ERROR, LICENSE_NOT_FOUND


# Returns license name and link by given license key.
def license_data(key):
	if not isinstance(key, str):
		raise TYPE_ERROR
	if key == 'bsd-2-clause':
		name = 'BSD 2-Clause License'
		link = OPEN_SOURCE_ORG + 'BSD-2-Clause'
	elif key == 'bsd-3-clause':
		name = 'BSD 3-Clause License'
		link = OPEN_SOURCE_ORG + 'BSD-3-Clause'
	elif key == 'agpl-3.0':
		name = 'GNU Affero General Public License v3.0'
		link = GNU_ORG + 'agpl-3.0'
	elif key == 'gpl-2.0':
		name = 'GNU General Public License v2.0'
		link = GNU_ORG + 'gpl-2.0'
	elif key == 'gpl-3.0':
		name = 'GNU General Public License v3.0'
		link = GNU_ORG + 'gpl-3.0'
	elif key == 'lgpl-2.1':
		name = 'GNU Lesser General Public License v2.1'
		link = GNU_ORG + 'lgpl-2.1'
	elif key == 'lgpl-3.0':
		name = 'GNU Lesser General Public License v3.0'
		link = GNU_ORG + 'lgpl-3.0'
	elif key == 'apache-2.0':
		name = 'Apache License Version 2.0'
		link = OPEN_SOURCE_ORG + 'Apache-2.0'
	elif key == 'epl-2.0':
		name = 'Eclipse Public License - v2.0'
		link = OPEN_SOURCE_ORG + 'EPL-2.0'
	elif key == 'mit':
		name = 'MIT License'
		link = OPEN_SOURCE_ORG + 'MIT'
	elif key == 'mpl-2.0':
		name = 'Mozilla Public License Version 2.0'
		link = OPEN_SOURCE_ORG + 'MPL-2.0'
	elif key == 'unlicense':
		name = 'Unlicense'
		link = 'http://unlicense.org'
	elif key == 'aal':
		name = 'Attribution Assurance License'
		link = OPEN_SOURCE_ORG + 'AAL'
	elif key == 'afl-3.0':
		name = 'Academic Free License 3.0'
		link = OPEN_SOURCE_ORG + 'AFL-3.0'
	elif key == 'apsl-2.0':
		name = 'Apple Public Source License 2.0'
		link = 'https://opensource.apple.com/apsl'
	elif key == 'artistic-2.0':
		name = 'Artistic License 2.0'
		link = OPEN_SOURCE_ORG + 'Artistic-2.0'
	elif key == 'bsl-1.0':
		name = 'Boost Software License 1.0'
		link = OPEN_SOURCE_ORG + 'BSL-1.0'
	elif key == 'catosl-1.1':
		name = 'Computer Associates Trusted Open Source License 1.1'
		link = OPEN_SOURCE_ORG + 'CATOSL-1.1'
	elif key == 'cecill-2.1':
		name = 'CeCILL License 2.1'
		link = OPEN_SOURCE_ORG + 'CECILL-2.1'
	else:
		raise LICENSE_NOT_FOUND
	return name, link


def download_content(url):
	
	# Check if url is of type string.
	if not isinstance(url, str):
		return TYPE_ERROR
	
	# Download content from https://github.com/YuriyLisovskiy/licenses.
	response = requests.get(url)
	if response.status_code == 200:

		# Decode response.
		json_data = json.loads(response.text)
		content = json_data.get('content')
		if content is not None:
	
			# Decode content using base64 encoding.
			decoded_data = base64.b64decode(content)
			return decoded_data
		return None
	elif response.status_code == 404:
		raise LICENSE_NOT_FOUND
