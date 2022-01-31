#!/usr/bin/env bash

ROOT_DIR=$(pwd)

if [ ! -d $ROOT_DIR/certs ]; then
    mkdir -p $ROOT_DIR/certs
else
    rm -f $ROOT_DIR/certs/*
fi

cd $ROOT_DIR/certs
openssl req -x509 -outform pem -out chain.pem -keyout privkey.pem \
    -newkey rsa:4096 -nodes -sha256 -days 3650 \
    -subj '/CN=localhost' -extensions EXT -config <(
        printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth"
    )
cat chain.pem >fullchain.pem
cd -

exit 0
