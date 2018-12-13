#!/bin/bash
#   Exports pin to userspace
echo "4" > /sys/class/gpio/export                  

# Sets pin 18 as an output
echo "out" > /sys/class/gpio/gpio4/direction


echo "0" > /sys/class/gpio/gpio4/value 

