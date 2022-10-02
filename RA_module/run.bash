#!/bin/bash

# Use  ./run.bash [version]

IMAGENAME=ra_project

VERSION=latest
if [ ! "$1" == "" ]; then
  VERSION=$1
fi

# change setings here if needed
PLAYGROUND_FOLDER=$HOME/playground
PNP_FOLDER=$HOME/src/PetriNetPlans
DEMO_FOLDER=`pwd`


echo "Running image $IMAGENAME:$VERSION ..."

if [ -d /usr/lib/nvidia-384 ]; then
  NVIDIA_STR="-v /usr/lib/nvidia-384:/usr/lib/nvidia-384 \
           -v /usr/lib32/nvidia-384:/usr/lib32/nvidia-384 \
           --device /dev/dri"
  echo "Nvidia support enabled"
fi

docker run -it \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/.Xauthority:/home/robot/.Xauthority:rw \
    $NVIDIA_STR \
    -e DISPLAY=$DISPLAY \
    --privileged \
    --net=host \
    -v $PLAYGROUND_FOLDER:/home/robot/playground \
    -v $DEMO_FOLDER/ra_action:/home/robot/src/ra_action \
    -v $DEMO_FOLDER/ra_action_msgs:/home/robot/src/ra_action_msgs \
    -v $DEMO_FOLDER/ra_pnp:/home/robot/src/ra_pnp \
    $IMAGENAME:$VERSION

# Add this if you want to mount also PetriNetPlans
#    -v $PNP_FOLDER:/home/robot/src/PetriNetPlans \

