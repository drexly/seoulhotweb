# -*- coding: utf-8 -*-
import codecs

import datetime
import os
from seoulhotver2.settings import BASE_DIR
from .models import SubwayModel,dbModel
qs=dbModel.objects.all()
f=[]
for a in qs:
    f.append(str(a))


def container():
    daytmp=str(datetime.datetime.now()).split(' ')
    date=daytmp[0][5:10]
    time=int(daytmp[1][0:2])
    # print date
    # print time
    #print f
    for i in f:
        i = i.split()
        a = SubwayModel(date=i[0], line_number=i[1], station=i[2], in_out=i[3],
                        population0=i[4],population1=i[5],population2=i[6],population3=i[7],population4=i[8],
                        population5=i[9],population6=i[10],population7=i[11],population8=i[12],population9=i[13],
                        population10=i[14],population11=i[15],population12=i[16],population13=i[17],population14=i[18],population15=i[19],
                        population16=i[20],population17=i[21],population18=i[22],population19=i[23],population20=i[24],population21=i[25],
                        population22=i[26],population23=i[27])
        a.save()
