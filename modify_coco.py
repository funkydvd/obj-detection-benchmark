import os

folder = "./test"

#person
#bike
#car
#motor
#bus
#train
#truck
#traffic light
#traffic sign


good = {}
good[0] = 0
good[1] = 1
good[2] = 2
good[3] = 3
good[5] = 4
good[6] = 5
good[7] = 6
good[9] = 7
good[11] = 8


for root, dirs, files in os.walk(folder):
        listf = files
        
for x in listf:
    file = open(os.path.join(folder,x),"r")
    file2 = open( os.path.join(folder,x) + "2", "w")
    lines = file.readlines()
    for line in lines:
        splitted = line.split(" ")
        #print (splitted)
        if int(splitted[0]) in good.keys():
            file2.write(str(good[int(splitted[0])]) + " ")
            for i in range(len(splitted)-2):
                file2.write(splitted[i+1]+" ")
            file2.write(splitted[len(splitted)-1])

    file.close()
    file2.close()
    os.remove(os.path.join(folder,x))
    os.rename( os.path.join(folder,x) + "2", os.path.join(folder,x))
