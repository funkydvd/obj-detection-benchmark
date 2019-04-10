import json
from pprint import pprint
from shutil import copyfile

day_sunny = []
day_overcast = []
day_snowy = []
day_rain = []
dusk_sunny = []
dusk_overcast = []
dusk_snowy = []
dusk_rain = []
night_sunny = []
night_overcast = []
night_snowy = []
night_rain = []

files = ["bdd100k_labels_images_val.json", "bdd100k_labels_images_train.json"]
srcs = ["images/100k/val/","images/100k/train/"]

i = -1
for file in files:
    i = i + 1
    with open(file) as f:
        data = json.load(f)
        for x in data:
            if x["attributes"]["weather"] == "clear" and  x["attributes"]["timeofday"] == "daytime":
                day_sunny.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "day_sunny/" +  x["name"]
             $   copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "overcast" and  x["attributes"]["timeofday"] == "daytime":
                day_overcast.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "day_overcast/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "rainy" and  x["attributes"]["timeofday"] == "daytime":
                day_rain.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "day_rain/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "snowy" and  x["attributes"]["timeofday"] == "daytime":
                day_snowy.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "day_snowy/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "clear" and  x["attributes"]["timeofday"] == "dawn/dusk":
                dusk_sunny.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "dusk_sunny/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "overcast" and  x["attributes"]["timeofday"] == "dawn/dusk":
                dusk_overcast.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "dusk_overcast/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "rainy" and  x["attributes"]["timeofday"] == "dawn/dusk":
                dusk_rain.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "dusk_rain/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "snowy" and  x["attributes"]["timeofday"] == "dawn/dusk":
                dusk_snowy.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "dusk_snowy/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "clear" and  x["attributes"]["timeofday"] == "night":
                night_sunny.append(x)
                src_file =srcs[i] + x["name"]
                dest_file = "night_sunny/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "overcast" and  x["attributes"]["timeofday"] == "night":
                night_overcast.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "night_overcast/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "rainy" and  x["attributes"]["timeofday"] == "night":
                night_rain.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "night_rain/" +  x["name"]
                copyfile(src_file,dest_file)
            if x["attributes"]["weather"] == "snowy" and  x["attributes"]["timeofday"] == "night":
                night_snowy.append(x)
                src_file = srcs[i] + x["name"]
                dest_file = "night_snowy/" +  x["name"]
                copyfile(src_file,dest_file)

print (len(day_sunny))
print (len(day_overcast))
print (len(day_snowy))
print (len(day_rain))
print (len(dusk_sunny))
print (len(dusk_overcast))
print (len(dusk_snowy))
print (len(dusk_rain))
print (len(night_sunny))
print (len(night_overcast))
print (len(night_snowy))
print (len(night_rain))

with open('day_sunny.json', 'w') as outfile:
    json.dump(day_sunny, outfile)
with open('day_overcast.json', 'w') as outfile:
    json.dump(day_overcast, outfile)
with open('day_snowy.json', 'w') as outfile:
    json.dump(day_snowy, outfile)
with open('day_rain.json', 'w') as outfile:
    json.dump(day_rain, outfile)
with open('dusk_sunny.json', 'w') as outfile:
    json.dump(dusk_sunny, outfile)
with open('dusk_overcast.json', 'w') as outfile:
    json.dump(dusk_overcast, outfile)
with open('dusk_snowy.json', 'w') as outfile:
    json.dump(dusk_snowy, outfile)
with open('dusk_rain.json', 'w') as outfile:
    json.dump(dusk_rain, outfile)
with open('night_sunny.json', 'w') as outfile:
    json.dump(night_sunny, outfile)
with open('night_overcast.json', 'w') as outfile:
    json.dump(night_overcast, outfile)
with open('night_snowy.json', 'w') as outfile:
    json.dump(night_snowy, outfile)
with open('night_rain.json', 'w') as outfile:
    json.dump(night_rain, outfile)        
            
