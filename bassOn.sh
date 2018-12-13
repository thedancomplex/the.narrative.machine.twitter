#!/bin/bash
#   Exports pin to userspace
echo "4" > /sys/class/gpio/export                  

# Sets pin 18 as an output
echo "out" > /sys/class/gpio/gpio4/direction


# Sets pin 18 to high
while [ 1 -lt 2 ]
do
echo "1" > /sys/class/gpio/gpio4/value

sleep 1
# Sets pin 18 to low
echo "0" > /sys/class/gpio/gpio4/value 

sleep 1
done
