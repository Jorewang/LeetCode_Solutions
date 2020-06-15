import os

path = "F:\download\大咖读书会"

f = os.listdir(path)

for i in f:
    oldname = path + '\\' + i
    print(oldname)
    newname = path + '\\' + i.split('.')[0]
    print(newname)
    os.rename(oldname, newname)
print("Done")
