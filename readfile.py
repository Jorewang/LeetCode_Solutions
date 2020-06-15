path = "C:\\Users\\admin\\Desktop\\train.txt"
copy_path = "C:\\Users\\admin\\Desktop\\train_2.txt"


f1 = open(path, "r")
f2 = open(copy_path, "w")
for line in f1:
    t = line.split()
    print(line)
    t[2] = "1" if t[2] == "1" else "-1"
    s_new = "  ".join(t)
    print(s_new)
    print('-'*20)
    f2.write(s_new+"\n")
f1.close()
f2.close()
