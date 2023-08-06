# Sotoki

*Stack Overflow to Kiwix*

The goal of this project is to create a suite of tools to create
[zim](http://www.openzim.org) files required by
[kiwix](http://kiwix.org/) reader to make available [Stack Overflow](https://stackoverflow.com/)
offline (without access to Internet).

## Getting started

The use of btrfs as a file system is recommended (and required for stackoverflow)

Install non python dependencies:

```
sudo apt-get install jpegoptim pngquant gifsicle advancecomp python-pip python-virtualenv python-dev libxml2-dev libxslt1-dev libbz2-dev p7zip-full python-pillow gif2apng imagemagick
```


Create a virtual environment for python:

```
virtualenv --system-site-packages venv
```

Activate the virtual enviroment:

```
source venv/bin/activate
```


Install this lib:

```
pip install sotoki
```


```
sotoki <domain> <publisher> [--directory=<dir>] [--nozim] [--tag-depth=<tag_depth>] [--threads=<threads>] [--zimpath=<zimpath>] [--reset] [--reset-images] [--clean-previous] [--nofulltextindex] [--ignoreoldsite] [--nopic] [--no-userprofile]

```
You can use `sotoki -h` to have more explanation about these options


