from django.shortcuts import render
from django.views.generic import ListView
import sys
from django.db.models import Q
# from django.utils import timezone

#from datetime import datetime
import datetime
from .models import SubwayModel

import codecs
import operator
# Create your views here.
from urllib.request import urlopen



def SubwayLV(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/busy.html'

    qs = SubwayModel.objects.filter(date="2014-"+str(now.month)+'-'+str(now.day))

    biggest = 0

    if now.hour and (now.hour == 0):
        for query in qs:
            if query.population0 >  biggest:
                biggest = query.population0
        qs = qs.get(population0=biggest)

    elif now.hour and (now.hour == 1):
        for query in qs:
            if query.population1 >  biggest:
                biggest = query.population1
        qs = qs.get(population1=biggest)

    elif now.hour and (now.hour == 2):
        for query in qs:
            if query.population2 >  biggest:
                biggest = query.population2
        qs = qs.get(population2=biggest)

    elif now.hour and (now.hour == 3):
        for query in qs:
            if query.population3 >  biggest:
                biggest = query.population0
        qs = qs.get(population3=biggest)

    elif now.hour and (now.hour == 4):
        for query in qs:
            if query.population4 >  biggest:
                biggest = query.population4
        qs = qs.get(population4=biggest)

    elif now.hour and (now.hour == 5):
        for query in qs:
            if query.population5 >  biggest:
                biggest = query.population5
        qs = qs.get(population5=biggest)

    elif now.hour and (now.hour == 6):
        for query in qs:
            if query.population6 >  biggest:
                biggest = query.population6
        qs = qs.get(population6=biggest)

    elif now.hour and (now.hour == 7):
        for query in qs:
            if query.population7 >  biggest:
                biggest = query.population7
        qs = qs.get(population7=biggest)

    elif now.hour and (now.hour == 8):
        for query in qs:
            if query.population8 >  biggest:
                biggest = query.population8
        qs = qs.get(population8=biggest)

    elif now.hour and (now.hour == 9):
        for query in qs:
            if query.population9 >  biggest:
                biggest = query.population9
        qs = qs.get(population9=biggest)

    elif now.hour and (now.hour == 10):
        for query in qs:
            if query.population10 >  biggest:
                biggest = query.population10
        qs = qs.get(population10=biggest)

    elif now.hour and (now.hour == 11):
        for query in qs:
            if query.population11 >  biggest:
                biggest = query.population11
        qs = qs.get(population11=biggest)


    elif now.hour and (now.hour == 12):
        for query in qs:
            if query.population12 >  biggest:
                biggest = query.population12
        qs = qs.get(population12=biggest)

    elif now.hour and (now.hour == 13):
        for query in qs:
            if query.population13 >  biggest:
                biggest = query.population13
        qs = qs.get(population13=biggest)

    elif now.hour and (now.hour == 14):
        for query in qs:
            if query.population14 >  biggest:
                biggest = query.population14
        qs = qs.get(population14=biggest)

    elif now.hour and (now.hour == 15):
        for query in qs:
            if query.population15 >  biggest:
                biggest = query.population15
        qs = qs.get(population15=biggest)

    elif now.hour and (now.hour == 16):
        for query in qs:
            if query.population16 >  biggest:
                biggest = query.population16
        qs = qs.get(population16=biggest)

    elif now.hour and (now.hour == 17):
        for query in qs:
            if query.population17 >  biggest:
                biggest = query.population17
        qs = qs.get(population17=biggest)

    elif now.hour and (now.hour == 18):
        for query in qs:
            if query.population18 >  biggest:
                biggest = query.population18
        qs = qs.get(population18=biggest)

    elif now.hour and (now.hour == 19):
        for query in qs:
            if query.population19 >  biggest:
                biggest = query.population19
        qs = qs.get(population19=biggest)

    elif now.hour and (now.hour == 20):
        for query in qs:
            if query.population20 >  biggest:
                biggest = query.population20
        qs = qs.get(population20=biggest)

    elif now.hour and (now.hour == 21):
        for query in qs:
            if query.population21 >  biggest:
                biggest = query.population21
        qs = qs.get(population21=biggest)

    elif now.hour and (now.hour == 22):
        for query in qs:
            if query.population22 >  biggest:
                biggest = query.population22
        qs = qs.get(population22=biggest)

    elif now.hour and (now.hour == 23):
        for query in qs:
            if query.population23 >  biggest:
                biggest = query.population23
        qs = qs.get(population23=biggest)

    print(qs.station)

    context = {"station" : qs}

    return render(request, template_name, context)

def main(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/index.html'

    qs = SubwayModel.objects.filter(date="2014-"+str(now.month)+'-'+str(now.day))

    biggest = 0
    small_pk = 0
    values = 'query.population' + str(now.hour)
    for query in qs:
        if eval(values) > biggest:
            biggest = eval(values)
            small_pk = query.id
    qs = qs.get(id=small_pk)

    context = {"station" : qs}

    return render(request, template_name, context)

def subway_lazy(request):
    now = datetime.datetime.now()

    dayString = ['월', '화', '수', '목', '금', '토', '일']

    template_name  = 'subway/busy.html'

    qs = SubwayModel.objects.filter(date="2014-"+str(now.month)+'-'+str(now.day))

    smallest = 100000
    values = 'query.population' + str(now.hour)
    for query in qs:
        if eval(values) < smallest:
            smallest = eval(values)
            small_pk = query.id
    qs = qs.get(id=small_pk)

    context = { "stations" : qs }

    template_name = 'subway/lazy.html'

    print (qs.station)

    return render(request, template_name, context)

def subway_now(request):
    now = datetime.datetime.now()

    template_name  = 'subway/busy.html'

    qs1 = SubwayModel.objects.get(date="2014-"+str(now.month)+'-'+str(now.day), station='도림천(247)', in_out='승차')
    qs2 = SubwayModel.objects.get(date="2014-"+str(now.month)+'-'+str(now.day), station='도림천(247)', in_out='하차')
    print(qs1)
    'qs.population' + str(now.hour)
    a = eval('qs1.population' + str(now.hour))
    b = eval('qs2.population' + str(now.hour))
    context = { 'station1': qs1, 'station2' : qs2 , 'pop':a+b}

    template_name='subway/now.html'

    return render(request, template_name, context)


def lanking(request):
    now = datetime.datetime.now()

    template_name  = 'subway/busy.html'

    qs = SubwayModel.objects.filter(date="2014-"+str(now.month)+'-'+str(now.day))

def bsbusy(request):
    tm=str(datetime.datetime.now()).split(':')[0]+'시 현재 서울 핫플 순위'
    daytmp = str(datetime.datetime.now()).split(' ')
    date = daytmp[0][5:10]
    time = int(daytmp[1][0:2])
    #f = codecs.open('2014.txt', 'r', encoding='euc-kr')
    html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
    content = html.read().decode('utf-8')
    raw = content.split("\n")
    f = []
    for a in raw:
        f.append(str(a).replace("\ufeff", ''))
    dayString = ['월', '화', '수', '목', '금', '토', '일']
    todaylist = []
    '''
    def weekday(year, month, day):
        year_1 = year / 100
        year_2 = year - year_1 * 100
        return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
    '''

    def weekday(year, month, day):
        return dayString[datetime.date(year, month, day).weekday()]

    odds = []
    for index, line in enumerate(f):
        lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
        raw = lin.split('\t')
        rst = []
        if index % 2 == 0:
            for elemindex, elem in enumerate(raw):
                if elemindex == 0:
                    rst.append(str(elem))
                    ymd = str(elem).split('-')
                    rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                elif elemindex == 1:
                    rst.append(elem)
                elif elemindex == 2:
                    rst.append(elem)
                elif elemindex != 3:
                    rst.append(int(elem))
        else:
            tmp = []
            for elemindex, elem in enumerate(raw):
                if elemindex > 3:
                    tmp.append(int(elem))
            odds.append(tmp)
        if len(rst) is not 0:
            todaylist.append(rst)

    for id, td in enumerate(odds):
        for i, t in enumerate(td):
            todaylist[id][4 + i] += t

    exact = []
    for qry in todaylist:
        if qry[0].endswith(date):
            exact.append(qry)

    sortrst = sorted(exact, key=operator.itemgetter(time + 4), reverse=True)
    context={'time':time+5,'now':tm,'blist':sortrst}
    template_name = 'subway/1bz.html'
    return render(request, template_name, context)

def bsempty(request):
    tm=str(datetime.datetime.now()).split(':')[0]+'시 현재 서울 콜플 순위'
    daytmp = str(datetime.datetime.now()).split(' ')
    date = daytmp[0][5:10]
    time = int(daytmp[1][0:2])
    #f = codecs.open('2014.txt', 'r', encoding='euc-kr')
    html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
    content = html.read().decode('utf-8')
    raw = content.split("\n")
    f = []
    for a in raw:
        f.append(str(a).replace("\ufeff", ''))
    dayString = ['월', '화', '수', '목', '금', '토', '일']
    todaylist = []
    '''
    def weekday(year, month, day):
        year_1 = year / 100
        year_2 = year - year_1 * 100
        return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
    '''

    def weekday(year, month, day):
        return dayString[datetime.date(year, month, day).weekday()]

    odds = []
    for index, line in enumerate(f):
        lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
        raw = lin.split('\t')
        rst = []
        if index % 2 == 0:
            for elemindex, elem in enumerate(raw):
                if elemindex == 0:
                    rst.append(str(elem))
                    ymd = str(elem).split('-')
                    rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                elif elemindex == 1:
                    rst.append(elem)
                elif elemindex == 2:
                    rst.append(elem)
                elif elemindex != 3:
                    rst.append(int(elem))
        else:
            tmp = []
            for elemindex, elem in enumerate(raw):
                if elemindex > 3:
                    tmp.append(int(elem))
            odds.append(tmp)
        if len(rst) is not 0:
            todaylist.append(rst)

    for id, td in enumerate(odds):
        for i, t in enumerate(td):
            todaylist[id][4 + i] += t

    exact = []
    for qry in todaylist:
        if qry[0].endswith(date):
            exact.append(qry)

    sortrst = sorted(exact, key=operator.itemgetter(time + 4))
    context={'time':time+5,'now':tm,'blist':sortrst}
    template_name = 'subway/1bz.html'
    return render(request, template_name, context)

def bsmy(request):
    checked_value = request.POST.getlist('check')
    if checked_value:
        print(checked_value)

        daytmp = str(datetime.datetime.now()).split(' ')

        ########검색에 필요한 인수들
        date = daytmp[0][5:10]
        time = int(daytmp[1][0:2])
        name = checked_value[0]
        #########################

        #f = codecs.open('2014.txt', 'r', encoding='euc-kr')
        html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
        content = html.read().decode('utf-8')
        raw = content.split("\n")
        f = []
        for a in raw:
            f.append(str(a).replace("\ufeff", ''))
        dayString = ['월', '화', '수', '목', '금', '토', '일']
        todaylist = []
        '''
        def weekday(year, month, day):
            year_1 = year / 100
            year_2 = year - year_1 * 100
            return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
        '''

        def weekday(year, month, day):
            return dayString[datetime.date(year, month, day).weekday()]

        odds = []
        for index, line in enumerate(f):
            lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
            raw = lin.split('\t')
            rst = []
            if index % 2 == 0:
                for elemindex, elem in enumerate(raw):
                    if elemindex == 0:
                        rst.append(str(elem))
                        ymd = str(elem).split('-')
                        rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                    elif elemindex == 1:
                        rst.append(elem)
                    elif elemindex == 2:
                        rst.append(elem)
                    elif elemindex != 3:
                        rst.append(int(elem))
            else:
                tmp = []
                for elemindex, elem in enumerate(raw):
                    if elemindex > 3:
                        tmp.append(int(elem))
                odds.append(tmp)
            if len(rst) is not 0:
                todaylist.append(rst)

        for id, td in enumerate(odds):
            for i, t in enumerate(td):
                todaylist[id][4 + i] += t

        exact = []
        for qry in todaylist:
            if qry[0].endswith(date) and str(qry[3]).__contains__(name):
                context=[daytmp,qry[2], qry[3], qry[time + 4],round((qry[time + 4]/qry[28])*100,2)]
                break

        return render(request, 'subway/3rst.html', {'context': context})
    return render(request, 'subway/3my.html', {'context': checked_value})

def source(request):
    return render(request, 'subway/2014.txt')

def bsvs(request):
    checked_value = request.POST.getlist('check')
    if checked_value:
        print(checked_value)
        daytmp = str(datetime.datetime.now()).split(' ')

        ########검색에 필요한 인수들
        date = daytmp[0][5:10]
        time = int(daytmp[1][0:2])
        names = checked_value
        #########################
        qq=''
        for ii,nm in enumerate(names):
            qq+=nm
            if ii < len(names)-1:
                qq+=' or '
        ##f = codecs.open('2014.txt', 'r', encoding='euc-kr')
        html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
        content = html.read().decode('utf-8')
        raw = content.split("\n")
        f = []
        for a in raw:
            f.append(str(a).replace("\ufeff", ''))

        dayString = ['월', '화', '수', '목', '금', '토', '일']
        todaylist = []
        '''
        def weekday(year, month, day):
            year_1 = year / 100
            year_2 = year - year_1 * 100
            return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
        '''

        def weekday(year, month, day):
            return dayString[datetime.date(year, month, day).weekday()]

        odds = []
        for index, line in enumerate(f):
            lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
            raw = lin.split('\t')
            rst = []
            if index % 2 == 0:
                for elemindex, elem in enumerate(raw):
                    if elemindex == 0:
                        rst.append(str(elem))
                        ymd = str(elem).split('-')
                        rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                    elif elemindex == 1:
                        rst.append(elem)
                    elif elemindex == 2:
                        rst.append(elem)
                    elif elemindex != 3:
                        rst.append(int(elem))
            else:
                tmp = []
                for elemindex, elem in enumerate(raw):
                    if elemindex > 3:
                        tmp.append(int(elem))
                odds.append(tmp)
            if len(rst) is not 0:
                todaylist.append(rst)

        for id, td in enumerate(odds):
            for i, t in enumerate(td):
                todaylist[id][4 + i] += t

        exact = []
        rst=[]
        for sts in names:
            for qry in todaylist:
                if qry[0].endswith(date) and str(qry[3]).__contains__(sts):
                    exact.append([qry[0], qry[1], qry[2], qry[3], qry[time + 4],qry[28]])

        sortrst = sorted(exact, key=operator.itemgetter(4), reverse=True)
        for ind, t in enumerate(sortrst):
            rst.append([str(ind + 1)+"위", t[2], t[3], t[4],t[5],round(t[4]/t[5]*100,2)])
        return render(request, 'subway/4rst.html', {'context': rst,'now':daytmp,'qq':qq})
    return render(request, 'subway/4vs.html', {'context': checked_value})
    #return render(request, 'subway/3rst.html', {'context': context})

def bscm(request):
    checked_value = request.POST.getlist('check')
    if checked_value:
        print(checked_value)
        daytmp = str(datetime.datetime.now()).split(' ')

        ########검색에 필요한 인수들
        date = daytmp[0][5:10]
        time = int(daytmp[1][0:2])
        name = checked_value[0]
        #########################

        #f = codecs.open('2014.txt', 'r', encoding='euc-kr')
        html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
        content = html.read().decode('utf-8')
        raw = content.split("\n")
        f = []
        for a in raw:
            f.append(str(a).replace("\ufeff", ''))
        dayString = ['월', '화', '수', '목', '금', '토', '일']
        todaylist = []
        '''
        def weekday(year, month, day):
            year_1 = year / 100
            year_2 = year - year_1 * 100
            return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
        '''

        def weekday(year, month, day):
            return dayString[datetime.date(year, month, day).weekday()]

        odds = []
        for index, line in enumerate(f):
            lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
            raw = lin.split('\t')
            rst = []
            if index % 2 == 0:
                for elemindex, elem in enumerate(raw):
                    if elemindex == 0:
                        rst.append(str(elem))
                        ymd = str(elem).split('-')
                        rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                    elif elemindex == 1:
                        rst.append(elem)
                    elif elemindex == 2:
                        rst.append(elem)
                    elif elemindex != 3:
                        rst.append(int(elem))
            else:
                tmp = []
                for elemindex, elem in enumerate(raw):
                    if elemindex > 3:
                        tmp.append(int(elem))
                odds.append(tmp)
            if len(rst) is not 0:
                todaylist.append(rst)

        for id, td in enumerate(odds):
            for i, t in enumerate(td):
                todaylist[id][4 + i] += t

        on = []
        off = []

        for qry in todaylist:
            if qry[0].endswith(date) and str(qry[3]).__contains__(name):
                "\n오늘 최적의 출근,등교시간\n"
                on.append(['5시', qry[9]])
                on.append(['6시', qry[10]])
                on.append(['7시', qry[11]])
                on.append(['8시', qry[12]])
                on.append(['9시', qry[13]])
                on.append(['10시', qry[14]])
                ons = sorted(on, key=operator.itemgetter(1))

                "\n오늘 최적의 퇴근,하교시간\n"
                off.append(['17시', qry[21]])
                off.append(['18시', qry[22]])
                off.append(['19시', qry[23]])
                off.append(['20시', qry[24]])
                off.append(['21시', qry[25]])
                offs = sorted(off, key=operator.itemgetter(1))
                break
        return render(request, 'subway/5rst.html', {'on': ons,'off': offs, 'now': daytmp,'name':name})
    return render(request, 'subway/3my.html', {'context': checked_value})

def bsfd(request):
    checked_value = request.POST.getlist('check')
    checked_val = request.POST.getlist('dday')

    if checked_value and checked_val:
        print(checked_value)
        print(checked_val)
        daytmp = str(datetime.datetime.now()).split(' ')

        ########검색에 필요한 인수들
        month = (daytmp[0][4:8])
        year = int(daytmp[0][0:4])
        day = (daytmp[0][9])
        time = int(daytmp[1][0:2])

        name = checked_value[0]
        dday = checked_val[0]
        #########################

        #f = codecs.open('2014.txt', 'r', encoding='euc-kr')
        html = urlopen("http://seoulhot.pythonanywhere.com/db/2014")
        content = html.read().decode('utf-8')
        raw = content.split("\n")
        f = []
        for a in raw:
            f.append(str(a).replace("\ufeff", ''))
        dayString = ['월', '화', '수', '목', '금', '토', '일']
        todaylist = []
        '''
        def weekday(year, month, day):
            year_1 = year / 100
            year_2 = year - year_1 * 100
            return dayString[(day + (month + 1) * 26 / 10 + year_2 + (year_2 / 4) + (year_1 / 4) - 2 * year_1 - 2) % 7]
        '''

        def weekday(year, month, day):
            return dayString[datetime.date(year, month, day).weekday()]

        odds = []
        for index, line in enumerate(f):
            lin = line[0:line.rfind(')') - 4] + line[line.rfind(')') + 1:]
            raw = lin.split('\t')
            rst = []
            if index % 2 == 0:
                for elemindex, elem in enumerate(raw):
                    if elemindex == 0:
                        rst.append(str(elem))
                        ymd = str(elem).split('-')
                        rst.append(weekday(int(ymd[0]), int(ymd[1]), int(ymd[2])))
                    elif elemindex == 1:
                        rst.append(elem)
                    elif elemindex == 2:
                        rst.append(elem)
                    elif elemindex != 3:
                        rst.append(int(elem))
            else:
                tmp = []
                for elemindex, elem in enumerate(raw):
                    if elemindex > 3:
                        tmp.append(int(elem))
                odds.append(tmp)
            if len(rst) is not 0:
                todaylist.append(rst)

        for id, td in enumerate(odds):
            for i, t in enumerate(td):
                todaylist[id][4 + i] += t

        exact = []
        value = []
        for i in range(1, 29):
            if weekday(year, int(month[1:3]), i) == dday:
                exact.append(i)
        for ind, qry in enumerate(todaylist):
            if qry[0][4:8] == month and str(qry[3]) == (name) and weekday(int(qry[0][0:4]), int(qry[0][5:7]),
                                                                          int(qry[0][8:10])) == dday:
                value.append(qry[28])
        sum = []

        for i in range(0, 4):
            sum.append([exact[i], value[i]])
        sortrst = sorted(sum, key=operator.itemgetter(1), reverse=True)

        return render(request, 'subway/6rst.html', {'yr': year, 'mth': month, 'dat': sortrst, 'dday': dday,'name':name})
    return render(request, 'subway/6fd.html', {'context': checked_value})
    
def bsch(request):
    return render(request, 'subway/chat.html')
    
def bssh(request):
    return render(request, 'subway/search.html')


