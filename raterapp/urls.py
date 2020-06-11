from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,  LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('new/project',views.new_project,name='new-project'),
    path('profile/',views.profile,name='profile'),
    path('new_profile/',views.new_profile,name = 'new_profile'),
    path('edit/profile/',views.profile_edit,name = 'edit_profile'),
    path('search/',views.search_project, name='search_results'),
    path('project/review/<project_id>',views.project_review,name='project_review'),


    path('accounts/login/',LoginView.as_view(redirect_authenticated_user=True,template_name='accounts/login.html'),name='login'),

    path('logout/',LogoutView.as_view(), name='logout'),
    path('accounts/register/',views.register, name='register'),

    path('api/profile/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)