#!/bin/bash
python system_interface.py &
sleep 1
echo Server up
python speech_interface.py -s deepspeech-0.9.3-models.pbmm -m deepspeech-0.9.3-models.scorer
killall Python