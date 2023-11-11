from django.shortcuts import render
from .forms import *

# Create your views here.
def home(request):
    form = ResumeForm()
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            #n1 = form.cleaned_data.get("fname")
            form.save()
            obj=form.instance
            return render(request,"home.html",{'form':form, "obj":obj})            
        else:
            return render(request, "home.html", {'form':form})
    else:        
        msg = 'Please fill all the fields'
        return render(request, "home.html", {'form':form, 'msg':msg})

def viewprofiles(request):
    if request.method == 'GET':
        rows = Profiles.objects.all()
        return render(request, 'viewprofiles.html', {'rows' : rows})

