import re
import json 
file = open("result_yolo_dusk_snow.txt","r")
data = file.readlines()
rez = []
i = 0
for i in range(len(data)):
    line = data[i]
    myre = re.compile('[a-zA-Z0-9-._]+')
    words = myre.findall(line)
    #words = re.split(':| |,|\t',line)
    if len(words)>0:
        if words[0]=='Enter' and len(words)>=4:
            entry = {}
            name = words[4]
            entry['name'] = name
            labels =  []
            j = i + 1
            while myre.findall(data[j])[0]!="Enter":
                words_2 = myre.findall(data[j])
                entry_2 = {}
                entry_2['name'] = words_2[0]
                if len(words_2)>=9:
                    offset = 0
                    begin = 2
                    while words_2[begin+offset]!="left_x":
                        offset = offset + 1
                    if offset>0:
                        cuv = ""
                        for ind in range(offset+1):
                            if ind>0:
                                cuv = cuv + " " + words_2[ind]
                            else:
                                cuv = words_2[ind]
                            #print (words_2[ind])
                        entry_2['name'] = cuv
                       # print (cuv)
                    #entry_2['name'] = words_2[0]
                    entry_2['x'] = words_2[3+offset]
                    entry_2['y'] = words_2[5+offset]
                    entry_2['width'] = words_2[7+offset]
                    entry_2['height'] = words_2[9+offset]
                    labels.append(entry_2)
                j = j+1
            entry['labels'] = labels
            rez.append(entry)
            
with open('result_yolo_dusk_snow.json', 'w') as outfile:
    json.dump(rez, outfile)   
            
        
