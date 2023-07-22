from django.shortcuts import render
# 响应到网页上
from django.http import HttpResponse
from .models import *
import os
import win32con
import win32api
from django.shortcuts import render
from .models import Station
from django.shortcuts import redirect
# Create your views here.
# 响应登录和注册,暂时还不知道别处需不需要配置


def login(request):
    return render(request, 'manage_soft/login.html')


def register(request):
    return render(request, 'manage_soft/register.html')


def regist_sql(request):
    ob = Users()
    ob.username = request.POST.get('username')
    # print(ob.username)
    try:
        user = Users.objects.get(username=ob.username)
        return HttpResponse('''<script> alert("用户已被注册");location.href = "login/register";</script>''')
    except:
        ob.password = request.POST.get('password')
        rightnum = request.POST.get('permission')
        if (rightnum == '0001'):
            ob.permission = '任务操作人员'
        else:
            ob.permission = '普通工作人员'
        ob.save()
        return HttpResponse('''<script> alert("注册成功！~");location.href = "/";</script>''')
# 更新


def select(request):
    return render(request, 'manage_soft/station.html')


def flash(request):
    ulist = Station.objects.all()
    context = {'stationlist': ulist}
    return render(request, 'manage_soft/station.html', context)


def login_judge(request):
    # return render(request, "manage_soft/login_judge.html")
    user = Users.objects.get(username=request.POST.get('username'))
    # rightnum = request.POST.get('permission')
    if request.POST['password'] == user.password:
        ulist = Station.objects.all()
        rightnum = 0
        if user.permission == '任务操作人员':
            rightnum = 1
        if user.permission == '普通工作人员':
            rightnum = 2
        context = {'stationlist': ulist, 'rightnum': rightnum}
        print(context)
        return render(request, 'manage_soft/station.html', context)
        # return HttpResponse('<script> location.href = "";</script>')
    else:
        return HttpResponse('<script> alert("账号或密码错误");location.href = "/";</script>')


def muchao(request, station_id=0, rightnum=0):
    muchao_info = info_muchao.objects.filter(station_id=station_id).last()
    context = {'last_data': muchao_info,
               'station_id': station_id, 'rightnum': rightnum}
    return render(request, 'manage_soft/GCS.html', context)


def station(request, station_id=0, rightnum=0):
    # return render(request, 'manage_soft/station.html')
    # print(station_name)
    station_info = UAV_message.objects.filter(station_id=station_id).last()
    print(station_info)
    context = {'last_data': station_info,
               'station_id': station_id,
               'rightnum': rightnum,
               }
    print(context)
    print(rightnum)
    if rightnum == 1:
        return render(request, 'manage_soft/UAV_manage.html', context)
    if rightnum == 2:
        return render(request, 'manage_soft/UAV.html', context)


def mission_go(request, station_id=0, rightnum=0):
    ob = mission()
    ob.station_id = station_id
    ob.Chang = request.POST.get('Chang')
    ob.Wei = request.POST.get('Wei')
    ob.Path = request.POST.get('path')
    ob.save()
    win32api.MessageBox(0, '任务发布成功', '中广核', win32con.MB_OK)
    station_info = UAV_message.objects.filter(station_id=station_id).last()
    # print(station_info)
    context = {'last_data': station_info,
               'station_id': station_id, 'rightnum': rightnum}
    if rightnum == 1:
        return render(request, 'manage_soft/UAV_manage.html', context)
    if rightnum == 2:
        return render(request, 'manage_soft/UAV.html', context)


def picture(request, station_id=0):
    ulist = Station.objects.get(station_id=station_id)
    # print(type(ulist))
    date = int(request.POST.get('Pic_date'))
    year = int(date/10000)
    month = int(date/100 % 100)
    if(month < 10):
        month1 = '0'+str(month)
    else:
        month1 = str(month)

    day = int(date % 100)
    if(day < 10):
        day1 = '0'+str(day)
    else:
        day1 = str(day)

    givedate = str(year)+"-"+month1+"-"+day1
    path = 'E:MYWEB_01\\static'+"\\"+str(ulist.station_name)+"\\"+givedate
    file_name_list = os.listdir(path)
    file_name = []
    # file_name = file_name.replace("[", "").replace("]", "").replace("'", "").replace(",", "\n").replace(" ", "")
    length = len(file_name_list)
    Chang = request.POST.get('Pic_Chang')
    Wei = request.POST.get('Pic_Wei')
    date_from = request.POST.get('Pic_date')
    print(date_from)
    context = {'station_name': ulist, 
               'length': length,
               'chang': Chang, 'wei': Wei, 'date_from': date_from}
    print(context)
    return render(request, 'manage_soft/picture.html', context)


def add(request):
    return render(request, 'manage_soft/station_add.html')


def delete(request):
    return render(request, 'manage_soft/station_del.html')


def add_to_sql(request):
    ob = Station()
    ob.station_name = request.POST.get('station_name')
    ob.station_id = request.POST.get('station_id')
    ulist = Station.objects.all()
    context = {'stationlist':ulist}
    try:
        user = Station.objects.get(station_name=ob.station_name)
        return HttpResponse('''<script> alert("此站台已经存在！");location.href="station/add";</script>''')
    except:
        ob.save()
        return HttpResponse('''<script> alert("站台添加成功");location.href="flash";</script>''')
        # return redirect('flash')
        # return render(request,'manage_soft/station.html',context)


def delete_to_sql(request):
    ob = Station()
    ob.station_name = request.POST.get('station_name')
    ob.station_id = request.POST.get('station_id')
    try:
        user = Station.objects.get(station_name=ob.station_name)
        user.delete()
        return HttpResponse('''<script> alert("站台删除成功");location.href="flash";</script>''')
    except:
        # ob.delete()
        return HttpResponse('''<script> alert("此站台不存在！");location.href="station/delete";</script>''')
