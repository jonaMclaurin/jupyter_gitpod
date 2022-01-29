#!/bin/bash

for f in $(cat $1); do
    if [[ $(file -b f) == +(PNG|gif) ]]
    then
        mv $f DeepLearning/week3/images
    else 
        mv $f DeepLearning/week3/
    fi
done