#!/bin/bash

set -e

for i in "$@"
do
  case $i in
    -v=*|--version=*)
      NEW_VERSION="${i#*=}"
      shift
    ;;
    -d=*|--dest=*)
      DEST_DIR="${i#*=}"
      shift
    ;;
    -s=*|--src=*)
      SOURCE_DIR="${i#*=}"
      shift
    ;;
    -r=*|--release=*)
      RELEASE_TAG="${i#*=}"
      shift
    ;;
    *)

    ;;
  esac
done

if [[ -n $1 ]]; then
    REPO=$1
fi

git clone ${REPO} ${SOURCE_DIR}

cd ${SOURCE_DIR}

# Generate DEB changelog
export RELEASE_TAG=${RELEASE_TAG}
./autogen.sh
./configure
make debian/changelog

# Generate deb package
debuild -us -uc

# Copy deb and src packages to dest dir
cp ../*.deb ${DEST_DIR}
cp ../*.tar.gz ${DEST_DIR}

exit 0
