#!/bin/bash

# prerequire
yum -y install gcc automake autoconf libtool make
yum install gcc gcc-c++

# source directory
SOURCE_DIR=/usr/local/src

pcre () {
  # install pcre for rewrite
	echo 'install pcre'
  cd $SOURCE_DIR
	wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.38.tar.gz
  tar -zxf pcre-8.38.tar.gz
  cd pcre-8.38
  ./configure
  make
  make install
	cd -
}

zlib () {
	# install zlib for gzip compress
	echo 'install zlib'
  cd $SOURCE_DIR

	wget http://zlib.net/zlib-1.2.8.tar.gz
	tar -zxf zlib-1.2.8.tar.gz
	cd zlib-1.2.8
	./configure
	make
	make install
	cd -
}

ssl () {
	echo 'install ssl'
  cd $SOURCE_DIR
	wget http://www.openssl.org/source/openssl-1.0.1c.tar.gz
	tar -zxf openssl-1.0.1c.tar.gz
	cd -
}

nginx () {
	echo 'install nginx'
  cd $SOURCE_DIR
  wget http://nginx.org/download/nginx-1.8.1.tar.gz
  tar -zxf nginx-1.8.1.tar.gz
  cd nginx-1.8.1

  ./configure --sbin-path=/usr/local/nginx/nginx \
  	--conf-path=/usr/local/nginx/nginx.conf \
  	--pid-path=/usr/local/nginx/nginx.pid \
  	--with-http_ssl_module \
  	--with-pcre=/usr/local/src/pcre-8.38 \
  	--with-zlib=/usr/local/src/zlib-1.2.8 \
  	--with-openssl=/usr/local/src/openssl-1.0.1c

  make
  make install
	cd -
}

pcre
zlib
ssl
nginx
