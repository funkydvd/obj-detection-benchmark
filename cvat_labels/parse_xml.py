import xml.etree.ElementTree as ET
import re
import json

labels = []
for i in range(13002):
    labels.append([])
        
for xi in range(8):
    name = "poli_dataset" + str(xi) + ".xml"
    tree = ET.parse(name)
    root = tree.getroot()
    offset = xi*1800
    print(offset)
  
    for neighbor in root.iter('track'):
        print (neighbor.attrib)
        print (neighbor.get('label'))
        for child in neighbor:
            if child.get('occluded')=='0':
                
                entry = {}
                entry['category'] =  neighbor.get('label')
                box2d = {}
                box2d['x1'] = child.get('xtl')
                box2d['x2'] = child.get('xbr')
                box2d['y1'] = child.get('ytl')
                box2d['y2'] = child.get('ybr')
                entry['box2d']=box2d
                labels[int(child.get('frame'))+offset].append(entry)

dict1 = {}
dict1['car']=0
dict1['person']=1
dict1['sign'] =2
dict1['rider']=3
dict1['bike']=4
final_json = []
for i in range(13001):
    entry = {}
    name = "frame" + str(i) + ".jpg" 
    name2 = "Output/frame" + str(i) + ".txt"
    fil = open(name2,"w")
    for j in labels[i]:
       fil.write(str(dict1[j['category']])+ " " + str(j['box2d']['x1']) + " " + str(j['box2d']['y1']) +  " " + str(int(float(j['box2d']['x2']) - float(j['box2d']['x1']))) + " " + str(int(float(j['box2d']['y2'])-float(j['box2d']['y1'])))+"\n")
    fil.close()
    entry['name']=name
    entry['labels']=labels[i]
   # print (entry)
    final_json.append(entry)
jsonf = open("final_json.json","w")
json.dump(final_json, jsonf)
jsonf.close()
#print (final_json)
