import re
import json
import math

files =  ["day_sunny","day_overcast","day_rain",
          "day_snow","dusk_sunny","dusk_overcast",
          "dusk_rain","dusk_snow", "night_sunny", "night_overcast",
          "night_rain", "night_snow"]

results = open("results/results_yolo2cat.txt", "w")
for f in files:
    f1 = open("result_yolo_" + f + ".json","r")
    f2 = open(f + ".json","r")

    data1 = json.load(f1)
    data2 = json.load(f2)

   

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
   
    # metrics - trueP/ (trueP + falseP) - precision
    # - trueP/ (trueP + falseN) - hit rate
    # - trueP/ (trueP +falseN + falseP) - accuracy
    # for trueP : sum ( x1-x2)^2 + (y1-y2)^2 + (sqrt(w1)-sqrt(w2))^2 + (sqrt(h1)-sqrt(h2))^2
    labels = {}
    labels2 = {}
    sz1  = 0
   # print (len(data1))
    for entry in data1:
        sz1 += len(entry['labels'])
        for x in entry['labels']:
            if not labels.get(x['name']):
                labels[x['name']] = 1
                print(x['name'])
   # print (sz1)
    sz2  = 0
    for entry in data2:
        
        for x in entry['labels']:
            if x.get('box2d'):
                sz2+=1
                if not labels2.get(x['category']):
                    labels2[x['category']] = 1
                   # print(x['category'])
                    
    #print (sz2)
    #print("")
    dict1 = {}
    dict1['car'] = 'car'
    dict1['traffic sign'] = 'stop sign'
    dict1['traffic light'] = 'traffic light'
    dict1['person'] = 'person'
    dict1['motor'] = 'motorbike'
    dict1['bus'] = 'bus'
    dict1['truck'] = 'truck'
    dict1['bike'] = 'bicycle'
    dict1['train'] = 'train'
    dict1['rider'] = 'person'
    sz2 = 0
    #exit()
    IoU = []
    for i in range(19):
        IoU.append(0.05*(i+1))
    print (IoU)
    MaP = 0
    RaP = 0
    for iou in IoU:
        trueP = 0
        falseP1 = 0
        falseP2 = 0
        falseN = 0
        truepsz = []
        falsepsz = []
        falsensz = []
        for i in range(23):
            truepsz.append(0)
            falsepsz.append(0)
            falsensz.append(0)
    
        error = 0
        for entry in data1: # current guess
            #print (entry['name'])
            for entry2 in data2: #ground truth
                if entry2['name'] == entry['name']: #same image
                    vect = []
                    ok = []
                    wgts= []
                    hgts = []
                    possibleFalseP = []
                    for x in entry['labels']:
                        wgts.append(int(float(x['width'])))
                        hgts.append(int(float(x['height'])))
                        vect.append(0)
                        possibleFalseP.append(0)
                        if x['name'] == 'car' or x['name'] == 'person':
                            ok.append(1)
                        else:
                            ok.append(0)
                    for x in entry2['labels']: #iterate trough ground truth labels for current image
                        real_name = x['category']
                       # print (x['attributes']['occluded'])
                        if x.get('box2d') and (x['category'] == 'car' or x['category'] == 'person'):
                            #print (x['attributes']['occluded'] == False)
                            #if x['attributes']['occluded'] == False:
                                sz2+=1
                                x1r = float(x['box2d']['x1'])
                                y1r = float(x['box2d']['y1'])
                                x2r = float(x['box2d']['x2'])
                                y2r = float(x['box2d']['y2'])
                                hr = abs(y1r-y2r)
                                wr = abs(x1r-x2r)
                               # print (x1r, y1r, x2r, y2r)
                                procmax = 0
                                imax = -1
                                entrygood = {}
                                i = 0
                                for x2 in entry['labels']: #search curent label in the guess
                                    if True: #@dict1[real_name] == x2['name']:
                                       
                                        xi1 = max(float(x1r), float(x2['x']))
                                        xi2 = min(float(x2r), float(x2['x'])+float(x2['width']))
                                        yi1 = max(float(y1r), float(x2['y']))
                                        yi2 = min(float(y2r), float(x2['y'])+float(x2['height']))
                                                  
                                        if xi1 <= xi2 and yi1 <=yi2 and (xi2-xi1)*(yi2-yi1)/ ( (x2r-x1r)*(y2r-y1r) + float(x2['width'])*float(x2['height'] ) - (xi2-xi1)*(yi2-yi1) ) > procmax and vect[i] ==0:
                                            if dict1[real_name] == x2['name']:
                                                procmax = (xi2-xi1)*(yi2-yi1)/ ( (x2r-x1r)*(y2r-y1r) + float(x2['width'])*float(x2['height'] ) - (xi2-xi1)*(yi2-yi1))
                                                entrygood = x2
                                                imax = i
                                                
                                            else:
                                                possibleFalseP[i] = 1
                                    i = i+1
                                #print (procmax)
                                if  procmax >= iou:
                                    x1g = float(entrygood['x'])
                                    x2g = float(entrygood['x']) + float(entrygood['width'])
                                    y1g = float(entrygood['y'])
                                    y2g = float(entrygood['y']) + float(entrygood['height'])
                                    hg = float(entrygood['height'])
                                    wg = float(entrygood['width'])
                                    #print (x1g,y1g,hg,wg)
                                    vect[imax] = 1
                                    trueP += 1
                                    #print (trueP)
                                    error +=(x1g-x1r)**2 + (y1g-y1r)**2 + ( math.sqrt(wr) - math.sqrt(wg)) ** 2 + ( math.sqrt(hg) - math.sqrt(hr))** 2
                                    for tt in range(23):
                                        if int(hr*wr)<classes[tt]:
                                            truepsz[tt]+=1
                                            break
                                else:
                                    falseN += 1
                                    for tt in range(23):
                                        if int(hr*wr)<classes[tt]:
                                            falsensz[tt]+=1
                                            break
                                            
                    
                    for i in range(len(vect)):
                        if vect[i] == 0 and ok[i] ==1: # false positivie
                            if possibleFalseP[i] == 1:
                                falseP1 +=1
                            else:
                            	falseP2 +=1
                            for tt in range(23):
                                    if int(hgts[i]*wgts[i])<classes[tt]:
                                        falsepsz[tt]+=1
                                        break        
                    break
            
        falseP = falseP1+ falseP2
        MaP +=  trueP/(trueP+falseP)
        RaP += trueP/(trueP + falseN)
        
        results.write("file: " + f + "\n");
        results.write("IoU = " + str(iou) + "\n")
        totaltp=0
        totalfn=0
        for i in range(23):
           # print  (str(classes[i]))
            print (truepsz[i])
            print(falsensz[i])
            totaltp+=truepsz[i]
            totalfn+=falsensz[i]
            print(totaltp)
            print(totalfn)
            if truepsz[i]+falsensz[i]>0:
             #   print ( str(truepsz[i]/(truepsz[i]+falsensz[i])))
                stri = "recall for class " + str(classes[i]) + " is " + str(truepsz[i]/(truepsz[i]+falsensz[i])) + "\n"     
                results.write (stri)
        for i in range(23):
            if truepsz[i]+falsepsz[i]>0:
                stri = "precision for class " + str(classes[i]) + " is " + str(truepsz[i]/(truepsz[i]+falsepsz[i])) + "\n"       
                results.write (stri)
        
        print("file " + f);
        results.write("falseP1 = " + str(falseP1) + "\nfalseP2 = " + str(falseP2) + "\n")
        results.write ("trueP: " + str(trueP) + "\n")
        results.write  ("falseP: "+str(falseP)+ "\n")
        results.write  ("falseN: "+str(falseN)+ "\n")
        if trueP+falseN>0:
            results.write  ("recall = " + str(trueP/(trueP+falseN))+ "\n")
        if trueP+falseP>0:
            results.write  ("precission = " + str(trueP/(trueP+falseP))+ "\n")
        if trueP > 0:
            results.write  ("average prediction error: "+ str(error/ trueP) + "\n")
        results.flush()
    MaP = MaP / len(IoU)
    RaP = RaP / len(IoU)
    results.write("Map = " + str(MaP) + "\n")
    results.write("Rap = " + str(RaP) + "\n")
results.close()
