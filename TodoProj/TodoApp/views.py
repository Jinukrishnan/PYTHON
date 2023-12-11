from django.shortcuts import render,redirect
from.models import Task
from .forms import TodoForm
# Create your views here.
def index(req):
    disptask=Task.objects.all()
    if req.method=='POST':
        name=req.POST.get('task','')
        priority=req.POST.get('priority','')
        date=req.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        print("created")
    return render(req,'index.html',{'task':disptask})

# def details(req):
   
#     return render(req,'details.html',)
def Delete(req,taskid):
    task=Task.objects.get(id=taskid)
    if req.method=='POST':
        task.delete()
        return redirect('/')
    return render(req,'delete.html')


def update(req,id):
    task=Task.objects.get(id=id)
    f=TodoForm(req.POST or None,instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(req,'edit.html',{'f':f,'task':task})

