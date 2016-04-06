#README

* docker build -t imageName:tag .
* docker -i -t imageName:tag /bin/bash

plink -v -N -i alpine_ssh_key.ppk -D 127.0.0.1:32346 -P 32345 192.168.99.100