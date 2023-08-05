import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyoslapi",
    version="0.0.1",
    author="Yuriy Lisovskiy",
    author_email="yuralisovskiy98@gmail.com",
    description="An API which allows you to get license templates or license notices from your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YuriyLisovskiy/licenses/tree/master/api/python",
    packages=setuptools.find_packages(exclude=['tests', 'tests.unittest']),
    install_requires=['requests==2.19.1'],
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
