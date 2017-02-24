#tt for testing
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seoulhotver2.settings")
django.setup()
from urllib.request import urlopen
from subway.models import dbModel
html = urlopen("http://127.0.0.1:8000/db/2014")
content =  html.read().decode('utf-8')
raw=content.split("\n")
f=[]
for a in raw:
    f.append(str(a).replace("\ufeff",''))
for xx in f:
    obj = dbModel(record=xx)
    obj.save()
