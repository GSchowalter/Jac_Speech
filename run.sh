#!/bin/bash
python system_interface.py &
sleep 1
echo Server up
python speech_interface.py
killall Python