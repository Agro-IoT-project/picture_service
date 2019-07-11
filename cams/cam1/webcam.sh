#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H:%M:%S")
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
rm $SCRIPTPATH/img/*
parentname="$(basename "$(dirname "$SCRIPTPATH/webcam.sh")")"


fswebcam -r 640x480 -q -d /dev/video1 --no-banner "${SCRIPTPATH}/img/$DATE-$parentname.jpg" 2>&1 "${SCRIPTPATH}/log/output.log"
