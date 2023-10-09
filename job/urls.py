
from django.urls import path, include
from . import views
app_name='job'
urlpatterns = [
   path('', views.job_list,name='job_list' ),
   #path('<int:id>/', views.job_detail,name = 'job_detail' ),
   path('add_job/', views.add_job,name = 'add_job' ),

   path('<str:slug>/<int:id>', views.job_detail,name = 'job_detail' ),
]
