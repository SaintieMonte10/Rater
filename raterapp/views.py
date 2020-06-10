from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.models import User
from .models import Project,Profile
from .forms import ProjectForm,ProfileForm,VoteForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.



def home(request):
    all_projects = Project.fetch_all_images()
    return render(request,"Moringa_Project_Awards/index.html",{"all_images":all_projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = current_user
            user_image.save()
        return redirect('home')
    else:
        form = ProjectForm()
    return render(request,"main/new_project.html",{"form":form})