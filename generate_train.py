import os



folder_names = ["day_sunny", "day_overcast", "day_rain", "day_snowy",
                "dusk_sunny", "dusk_overcast", "dusk_rain", "dusk_snowy",
                "night_sunny", "night_overcast", "night_rain", "night_snowy"]
file_namesM = map(lambda x : "train_" + x + ".txt", folder_names)
file_names = list(map(str,file_namesM))
i = 0

for a in file_names:
    print (a)
for i in range(len(folder_names)):
    for root, dirs, files in os.walk(folder_names[i]):
        file = open(file_names[i],"w")
        for x in files:
            file.write(folder_names[i] + "/" + x + "\n");
        file.close()

