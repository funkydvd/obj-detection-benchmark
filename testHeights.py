import re
import json
import math

files =  ["day_sunny","day_overcast","day_rain",
          "day_snow","dusk_sunny","dusk_overcast",
          "dusk_rain","dusk_snow", "night_sunny", "night_overcast",
          "night_rain", "night_snow"]

sizes = []
for i in range(1280*720):
    sizes.append(0)
classes = []

classes.append(100)
classes.append(150)
classes.append(200)
classes.append(250)
classes.append(300)
classes.append(400)
classes.append(500)
classes.append(600)
classes.append(700)
classes.append(800)
classes.append(900)
classes.append(1000)
classes.append(1300)
classes.append(1600)
classes.append(2000)
classes.append(3000)
classes.append(4000)
classes.append(5000)
classes.append(7000)
classes.append(10000)
classes.append(20000)
classes.append(30000)
classes.append(1000000)

classessz = []
for i in range(23):
    classessz.append(0)
    
for f in files:

    f2 = open(f + ".json","r")
    data2 = json.load(f2)
    print(f2)
    for entry2 in data2: #ground truth
        for x in entry2['labels']: #iterate trough ground truth labels for current image
            real_name = x['category']
                    
            if x.get('box2d'):# and (x['category'] == 'car' or x['category'] == 'person'):
                x1r = float(x['box2d']['x1'])
                y1r = float(x['box2d']['y1'])
                x2r = float(x['box2d']['x2'])
                y2r = float(x['box2d']['y2'])
                hr = abs(y1r-y2r)
                wr = abs(x1r-x2r)
                sizes[int(hr*wr)]+=1
                for t in range(23):
                    if int(hr*wr)<classes[t]:
                        classessz[t]+=1
                        break

maxs = 0
maxd = 0
tots = 0
for i in range(1280*720):
    if sizes[i]>sizes[maxs]:
        maxs = i
    if sizes[i]>0:
        maxd = i
    tots += sizes[i]
    #if i%1000 == 0:
       # print (i,tots)

for i in range(23):
    print (classes[i],classessz[i])

classcom=[]
i = 0
t=0
while i<23:
    classcom.append(0)
    for j in range(4):
        classcom[t]+=classessz[i]
        i+=1
        if i>=23:
            break
    t+=1
for i in range(len(classcom)):
    print (i,classcom[i])
print(tots)
print (maxd)
print (maxs, sizes[maxs])
        
