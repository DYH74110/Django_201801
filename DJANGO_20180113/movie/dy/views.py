from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect  #跳转
import pandas as pd


# train = pd.read_csv(r"C:\Users\Administrator\Desktop\大数据竞赛-风险识别算法赛\train.csv",delimiter=',')


# Create your views here.
# 首页 自己新建
def index(request):
    # return HttpResponse('<h1>Hello word[index]</h1>')
    context={
        'name1':'战狼2',
        'name2':'英伦对决'
    }
    return render(request,'index.html',context=context)   #新建的文件夹一定是要：templates

def dyh(request):
    return HttpResponse('<h2>Hello,Diaoyuanhui</h2>')

def lht(request):
    return HttpResponse('<h1>Hello,Lihuiting.</h1>')