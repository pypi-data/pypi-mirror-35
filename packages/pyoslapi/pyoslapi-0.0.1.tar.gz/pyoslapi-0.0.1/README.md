### Python Open Source Licenses API

An API which allows you to get license templates or license notices from your
code.

### Installation
```
$ pip install pyoslapi
```

### Usage

Example:
```py
from pyoslapi.client import Client

if __name__ == '__main__':
	client = Client()
	license = client.get_license('apache-2.0')
	if license is not None:
		print(
			"Name: {}\nLink: {}\nContent:\n{}\n".format(
				license.name, license.link, license.content
			)
		)
	
	header = client.get_header('apache-2.0')
		if header is not None:
			print("Header: {}".format(header))
			
	license_list = client.get_list()
		if license_list is not None:
			print("License List: {}".format(license_list))

```
