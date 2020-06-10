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
    return render(request,"main/index.html",{"all_images":all_projects})


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

@login_required(login_url='/accounts/login/')
def profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        logged_user = Profile.objects.get(prof_user=request.user)
        form = ProfileForm(request.POST, request.FILES, instance=logged_user)
        if form.is_valid():
            form.save()
        return redirect('profile')
    else:
        form = ProfileForm()
    return render(request,'profile/edit_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user = current_user)

    try:   
        prof = Profile.objects.get(prof_user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request,'profile/profile.html',{'profile':prof,'projects':projects})
