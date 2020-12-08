import urllib.request
target_url = "https://nfulist.herokuapp.com/?semester=1091&courseno=0776"
cp1b = []
for line in urllib.request.urlopen(target_url):
    cp1b.append(int(line.decode('utf-8').rstrip()))
from random import shuffle
shuffle(cp1b)
n = 5
m = int(len(cp1b)/n)
list2 = []
for i in range(0,len(cp1b),m):
    list2.append(cp1b[i:i+m])
print(list2)