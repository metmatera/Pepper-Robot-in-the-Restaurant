#!/bin/bash

# Use  ./build.bash [Dockerfile] [version]

IMAGENAME=ra_project

DOCKERFILE=Dockerfile
if [ ! "$1" == "" ]; then
  DOCKERFILE=$1
fi

VERSION=latest
if [ ! "$2" == "" ]; then
  VERSION=$2
fi

docker build --no-cache -t $IMAGENAME:$VERSION -f $DOCKERFILE .

