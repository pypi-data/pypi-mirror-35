#!/bin/bash -e

. /var/cache/build/packages-manual/common.sh

download_and_verify \
    alexdobin \
    star \
    2.5.4b \
    bfa6ccd3b7b3878155a077a9c15eec5490dffad8e077ac93abe6f9bfa75bb2b4 \
    https://github.com/alexdobin/STAR/archive/\${version}.tar.gz \
    STAR-\${version}

rm -r doc
rm -r source
rm -r extras
rm -r bin/Linux_x86_64_static
rm -r bin/MacOSX_x86_64

add_binary_path \
    alexdobin \
    star \
    bin/Linux_x86_64
