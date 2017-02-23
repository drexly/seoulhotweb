#tt for testing
from urllib.request import urlopen
html = urlopen("http://127.0.0.1:8000/db/2014")
content =  html.read().decode('utf-8')
raw=content.split("\n")
f=[]
for a in raw:
    f.append(str(a).replace("\ufeff",''))
for xx in f:
    print (xx)