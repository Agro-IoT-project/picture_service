#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H:%M:%S")
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
rm $SCRIPTPATH/img/*
parentname="$(basename "$(dirname "$SCRIPTPATH/webcam.sh")")"

raspistill -o "${SCRIPTPATH}/img/$DATE-$parentname.jpg" 
