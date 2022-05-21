 import time
start_time = time.time()
x=[]
y=[]
with open("C:\\Users\\Ashu\\Desktop\\Project\\sample4\\result41.csv", 'r') as filehandle:  
    filecontents = filehandle.readlines()
    for line in filecontents:
        current_place = line[:-1]
        x.append(current_place)

with open("C:\\Users\\Ashu\\Desktop\\Project\\sample4\\Dictionary1.txt", 'r') as filehandle:  
    filecontents = filehandle.readlines()
    for line in filecontents:
        current_place = line[:-1]
        y.append(current_place)

s = open("C:\\Users\\Ashu\\Desktop\\Project\\sample4\\sample4.txt").read()
for i in range(len(x)):
    s = s.replace(y[i],x[i])
    f = open("C:\\Users\\Ashu\\Desktop\\Project\\sample4\\sample4.txt", 'w')
    f.write(s)
    f.close()
print(s)

elapsed_time = time.time() - start_time
print("Time Consumed : ",elapsed_time)
