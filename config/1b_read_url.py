import urllib.request
target_url = "https://nfulist.herokuapp.com/?semester=1091&courseno=0776"
cp1b = []
for line in urllib.request.urlopen(target_url):
    cp1b.append(line.decode('utf-8'))
print(cp1b)