#!/usr/bin/env bash
git clone https://github.com/svn2github/chdkptp.git
cd chdkptp
git checkout ce4c132a48364eefd0641b9d58927d06d5bb9ce3
mv config-sample-linux.mk config.mk
make

ln -s $(pwd)/chdkptp.sh /bin/chdkptp