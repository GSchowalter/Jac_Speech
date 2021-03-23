# Jac_Speech
Jac Speech is the voice interaction interfaced used on the JAC Cart autonomous vehicle research project being conducted at JMU.

# Dependencies and Installations

## Deep speech
- Mozilla Deep speech has a pretrained model that is used for voice recognition in this project
- When setting up the installation execute the following commands in a new python virtual environment
`pip install deepspeech`
`pip install -r requirements`
- You will also need to download two files from the deepspeech repository
`deepspeech-0.9.3-models.pbmm`
`deepspeech-0.9.3-models.scorer`

# Running the prototype
- two commands in differnt terminal windows
- `python3 speech_interface -m deepspeech-0.9.3-models.pbmm`
- `python system_interface`
- say "stop" to terminate the system_interface process and use ctrl-c to terminate the speech_interface process
