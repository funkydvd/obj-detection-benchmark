fi = open("poli2.txt","w")
for i in range(13001):
	txt = "/home/david/darknet/data/poli/images/val/frame" + str(i)+".jpg\n"
	fi.write(txt)
fi.close()
