##merging individual wavs
import os
import wave
import soundfile


path_to_dir = "/mnt/c/Users/ikola/Documents/tts/batch/out"

list_of_dirs = os.listdir(path_to_dir)
for dirs in list_of_dirs:
    the_numbers_list =  []
    list_in_files = []
    list_of_files = os.listdir(path_to_dir+"/"+dirs)
    for wavs in list_of_files:
        the_numbers = wavs.split(".wav")[0]
        the_numbers_list.append(int(the_numbers))
    the_numbers_list.sort(key=int)
    for things in the_numbers_list:
        list_in_files.append("out"+"/"+dirs+"/"+str(things)+".wav")  ###test needs to be changed later into the real dir
    infiles = list_in_files
    for files in infiles:
        #print(files)
        data, samplerate = soundfile.read(files)
        soundfile.write(files, data, samplerate, subtype="PCM_16")
    outfile = ("out"+"/"+dirs+".wav")###test needs to be changed later into the real dir
    data= []
    for infile in infiles:
        w = wave.open(infile, 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
        
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()