from re import A
import re

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from .forms import *
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
msg='''<h1 style="color:green;margin-top:300px;">This is my start page</h1>'''
# Create your views here.
def startpage(request,data):
    print(data)
    print(type(data))

    # return HttpResponse(msg)
    return HttpResponse("<h3>welcome {} </h3>".format(data))

def sample(request):
    name="Chaithre"
    context={'username':name}
    return render(request,'sample.html',context)

def startPage(request,data):
    
    return render(request,'startpage.html',{'data':data})

def viewreg(request):
    if request.method=='GET':
        return render(request,'reg.html')
    elif request.method=='POST':
        fname=request.POST['ffname']
        lname=request.POST['llname']
        age=request.POST['aage']
        place=request.POST['pplace']
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        rg=Reg()
        ul=UserLog()
        rg.fname=fname
        rg.lname=lname
        rg.age=age
        rg.place=place
        ul.username=uname
        ul.password=pswd
        ul.userid=rg
        rg.save()
        ul.save()
        print(fname,lname,age,place)
        # dic1={'firstname':fname,'lastname':lname,'age':age,'place':place}
        # return render(request,'regview.html',dic1)            #html page
        return redirect('viewdata')             #redirect  db ,table

def viewdata(request):
    ul=UserLog.objects.all()
    return render(request,'view.html',{'data':ul})

def editdata(request,id):
    ul=UserLog.objects.get(id=id)
    rg=ul.userid
    if request.method=='GET':
        print(id)
        
        return render(request,'editdata.html',{'data':ul})
    else:
        fname=request.POST['ffname']
        lname=request.POST['llname']
        age=request.POST['aage']
        place=request.POST['pplace']
        uname=request.POST['uname']
        pswd=request.POST['pswd']

        # rg=Reg()
        rg.fname=fname
        rg.lname=lname
        rg.age=age
        rg.place=place
        ul.username=uname
        ul.password=pswd
        rg.save()
        ul.save()
        return redirect('viewdata')  


def deletedata(request,id):
    rg=UserLog.objects.get(pk=id)
    rg.delete()
    return redirect('viewdata')

def statview(request):
    return render(request,'stat.html')

def large(request,data1,data2,data3):
   dic2={'val1':data1,'val2':data2,'val3':data3}
   return render(request,'large.html',dic2)

def RegFormView(request):
    if request.method=='GET':
        form=RegForm()
        return render(request,'regformview.html',{'form':form})

def viewmodelform(request):
    if request.method=='GET':
        form1=RegModelForm()
        form2=UserLogModelForm()
        return render(request,'viewmodelform.html',{'form1':form1,'form2':form2})
    elif request.method=='POST':
        form1=RegModelForm(request.POST)
        form2=UserLogModelForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            obj1=form1.save(commit=False)
            obj2=form2.save(commit=False)
            obj2.userid=obj1
            form1.save()
            form2.save()
            return redirect('viewdata')

def employee(request):
    if request.method=='GET':
        form3=EmployeeModelForm()
        return render(request,'employee.html',{'form3':form3})
    elif request.method=='POST':
        form3=EmployeeModelForm(request.POST)
        if form3.is_valid():
            form3.save()
            return redirect('viewemp')

def viewemp(request):
    emp=Employee.objects.all()
    return render(request,'viewemp.html',{'data1':emp})

# def uploadfile(request):
   
#     up=UploadFile()
#     if request.method=='GET':
#         return render(request,'fileupload.html')
#     elif request.method=='POST':
#         up.title=request.POST['title']
#         up.des=request.POST['des']
#         up.file=request.FILES['file']
#         up.save()
#         return render(request,'fileupload.html',{'msg':'successfully uploaded'})
def uploadfile(request):
    if 'username' in request.session:
        up=UploadFile()
        if request.method=='GET':
            return render(request,'fileupload.html')
        elif request.method=='POST':
            up.title=request.POST['title']
            up.des=request.POST['des']
            up.file=request.FILES['file']
            up.save()
            return render(request,'fileupload.html',{'msg':'successfully uploaded'})
    else:
        return redirect('ses')
def uploadimage(request):
    if request.method=='GET':
        form4= UploadImageModelForm()
        return render(request,'uploadimage.html',{'form4':form4})
    elif request.method=='POST':
        form4=UploadImageModelForm(request.POST,request.FILES)
        if form4.is_valid():
            form4.save()
            return render(request,'uploadimage.html',{'form4':form4,'msg':'successfully uploaded'})

class UploadFileListView(ListView):
    model=UploadFile
    template_name="filelistview.html"
    context_object_name="data"
class CreateFileView(CreateView):
    model=UploadImage
    fields='__all__'
    # form_class=UploadImageModelForm
    template_name='fileuploadmodelform.html'
    success_url=reverse_lazy('filelist')

class CreateFileModelView(CreateView):
    model=UploadFile
    form_class=UploadFileModelForm
    template_name="fileuploadmodelform.html"
    success_url=reverse_lazy("filelist")

def cookcreate(request):
    if request.method=='GET':
        resp=render(request,'setcook.html')
        resp.set_cookie('username','Anusree',max_age=5)
        resp.set_cookie('marks',90,max_age=5)
        # resp.set_cookie('username', value='Anusree', max_age=5)
        return resp

def readcook(request):
    if 'username' in request.COOKIES:
        name=request.COOKIES['username']
        return HttpResponse(name)
    else:
        return HttpResponse('COOKIE NOT SET')
def cookie_form(request):
    if request.method=='GET':
        name='Unknown'
        if 'name' in request.COOKIES:
            name=request.COOKIES['name']
        return render(request,'create_cookies.html',{'name':name})
    elif request.method=='POST':
        name=request.POST['name']
        resp=render(request,'create_cookies.html')
        resp.set_cookie('name',name)
        return resp

def sess_create(request):
    if request.method=='GET':
        return render(request,'sess_create.html')
    else:
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        request.session['username']=uname
        print(uname,pswd)
        return render(request,'sess_create.html')

def readsess(request):
    uname=request.session['username']
    return HttpResponse('<h3>{}</h3>'.format(uname))

def logoutuser(request):
    del request.session['username']
    return redirect('ses')

def ses_reg(request):
    if request.method=='GET':
        return render(request,'ses_reg.html')
    else:
        fname=request.POST['ffname']
        lname=request.POST['llname']
        age=request.POST['aage']
        place=request.POST['pplace']
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        rg=Register()
        rg.fname=fname
        rg.lname=lname
        rg.age=age
        rg.place=place
        rg.username=uname
        rg.password=pswd
        rg.save()
        print(fname,lname,age,place,uname,pswd)
        return render(request,'ses_reg.html')
def loginuser(request):
    if request.method=='GET':
        return render(request,'loginpage.html')
    else:
        uname=request.POST['uname']
        pswd=request.POST['pswd']
        print(uname,pswd)
        
        try:
            rg=Register.objects.get(username=uname,password=pswd)
            if rg:
                request.session['userid']=rg.id
                # return render(request,'loginpage.html')
                return redirect('details')
        except:
            return render(request,'loginpage.html',{'msg':'invalid username and password'})
        
        
def logout(request):
    try:
        if request.method=='GET':
            del request.session['username']
            return redirect('loginuser')
    except KeyError:
        return redirect('loginuser')

def details(rq):
    reg1=Register.objects.all()
    return render(rq,'viewregsession.html',{'data1':reg1})

def viewjsontable(request,user):
    print(user)
    try:
        uid=Register.objects.get(username=user)
        print(uid)
    except:
        return JsonResponse('',safe=False)
    else:
        return JsonResponse('Username already Exists',safe=False)