file = open('frames.txt',"w")
for i in range(13001):
    name = "frame" + str(i) + ".jpg\n"
    file.write(name)
file.close()
