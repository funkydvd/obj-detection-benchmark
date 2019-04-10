import re
import json

files = ["day_sunny", "day_overcast","day_rain","day_snowy",
         "dusk_sunny","dusk_overcast","dusk_rain","dusk_snowy",
         "night_sunny","night_overcast","night_rain","night_snowy"]
for fix in files:
    name = "result_retinanet_" + fix + ".txt"
    outf =  "result_retinanet_" + fix + ".json"
    file = open(name,"r")
    data = file.readlines()
    rez = []
    i = 0
    for i in range(len(data)):
        line = data[i]
        myre = re.compile('[a-zA-Z0-9-._]+')
        words = myre.findall(line)
        #words = re.split(':| |,|\t',line)
        if len(words)>0:
            if ".jpg" in words[0]:
                entry = {}
                name = words[0]
                entry['name'] = name
               # print (name)
                labels =  []
                j = i + 1
                if j < len(data):
                    while ".jpg" not in myre.findall(data[j])[0]:
                        words_2 = myre.findall(data[j])
                        entry_2 = {}
                        entry_2['name'] = words_2[4]
                        indix = 5
                        while indix < len(words_2):
                            entry_2['name'] = entry_2['name']+ " " + words_2[indix]
                            indix+=1
                            print (entry_2['name'])
                        entry_2['x'] = words_2[0]
                        entry_2['y'] = words_2[1]
                        entry_2['width'] = words_2[2]
                        entry_2['height'] = words_2[3]
                        labels.append(entry_2)
                        j = j+1
                        if j ==len(data):
                            break
                entry['labels'] = labels
                rez.append(entry)
                
    with open(outf, 'w') as outfile:
        json.dump(rez, outfile)   
                
        
