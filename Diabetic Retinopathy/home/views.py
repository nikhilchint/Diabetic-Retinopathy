from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact,DR
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import keras.utils as image
import tensorflow as tf
import json
from tensorflow import Graph
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

img_height, img_width=224,224
with open('./models/imagenet_classes.json','r') as f:
    labelInfo=f.read()

labelInfo=json.loads(labelInfo)

model_graph = Graph()
with model_graph.as_default():
    tf_session = tf.compat.v1.Session()
    with tf_session.as_default():
        model=load_model('./models/mobilnet_model.h5')
# Create your views here.
def index(request):
    # return HttpResponse("this is home page")
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def result(request):
    print(request)
    l=[]
    print(request.POST.dict())
    l=request.POST.dict()
    fileobj=request.FILES["right"]
    # print(fileobj)
    fileobj1=request.FILES["left"]
    fs=FileSystemStorage()
    fs1=FileSystemStorage()
    filepathname=fs.save(fileobj.name,fileobj)
    filepathname1=fs1.save(fileobj1.name,fileobj)
    filepathname=fs.url(filepathname)
    filepathname1=fs1.url(filepathname1)
    testimage='.'+filepathname
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)
    testimage='.'+filepathname1
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x=x/255
    x=x.reshape(1,img_height, img_width,3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi=model.predict(x)
    import numpy as np
    predictedLabel=labelInfo[str(np.argmax(predi[0]))]
    predictedLabel1=labelInfo[str(np.argmax(predi[0]))]
# 'predictedLabel':predictedLabel[1],'predictedLabel1':predictedLabel1[1],
    # k=0
    context={'filepathname':filepathname,'filepathname1':filepathname1,'predictedLabel':predictedLabel[1],'predictedLabel1':predictedLabel1[1],'l1':l['name'],'l2':l['email'],'l3':l['gender'],'l4':l['age'],'l5':l['phone']}
    print(context)
    det=DR(name1=l['name'],email1=l['email'],gender=l['gender'],age=l['age'],phone1=l['phone'],right=fileobj,left=fileobj1,rprediict=predictedLabel[1],lpredict=predictedLabel1[1])
    det.save()
    return render(request,'result.html',context)
def service(request):
    return render(request,'service.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        date=datetime.today()
        contact=Contact(name=name,email=email,desc=desc,date=date)
        contact.save()
        messages.success(request,'your message have been sent!')
    return render(request,'contact.html')
def detect(request):
   

    # if request.method=="POST" and request.FILES["right"]:
    #     # name=request.POST.get('name')
    #     # email=request.POST.get('email')
    #     # phone=request.POST.get('phone')
    # #     # date=datetime.today()
    #     # right=str(request.FILES["right"])
    #     left=str(request.FILES["left"])

    # #     # fd=FileSystemStorage()
    # #     # filename1=fd.save(right.name,right)
    # #     # uploaded_file_url=fd.url(filename1)
    # #     # print(uploaded_file_url)
    # # name1=name,email1=email,phone1=phone,right=right,
    #     det=DR(left=left)
    #     det.save()
    #     return render(request,'detect.html')
    #     messages.success(request,'your message have been sent!')
    return render(request,'detect.html')
def report(request):
    drlist=DR.objects.all()
    print(drlist)
    k=0
    return render(request,'report.html',{'drlist':drlist,'k':k})
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")