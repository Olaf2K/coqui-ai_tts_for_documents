# coqui-ai_tts_for_documents

Based on: https://tts.readthedocs.io/en/latest/index.html

Reads file line by line and turns into speech, after stitches everything together into one file

Tested on windows 11; WSL system: Ubuntu 20.04

Install TTS module by running 'pip install tts' #see https://tts.readthedocs.io/en/latest/inference.html for more instructions

Put the sentences you want to synthesize in one sentece per line in a file called 'in.txt'

Create a folder called "out". This hold the temporary audio files per sentence.

Run bash script synth_bash_TTS_0.2.0

Combined audio file is now deposited in the current directory