import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="klangooclient",
    version="1.0.0",
	license='MIT License',
    author="Klangoo",
    author_email="support@klangoo.com",
    description="Magnet API client driver for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Klangoo/MagnetApiClient.Python",
	keywords=['Klangoo', 'Magnet', 'MagnetApiClient', 'Http Client'],
    packages=setuptools.find_packages(),
    classifiers=[
		"Programming Language :: Python",
        "Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
		"Topic :: Internet :: WWW/HTTP",
    ],
)