
from django.urls import path, include
from . import views
from . import api
app_name='job'
urlpatterns = [
   path('', views.job_list,name='job_list' ),
   #path('<int:id>/', views.job_detail,name = 'job_detail' ),
   path('add_job/', views.add_job,name = 'add_job' ),

   path('<str:slug>/<int:id>', views.job_detail,name = 'job_detail' ),
   #apis
   path('api/all_jobs_api',api.api_job_list,name='all_jobs_api'),
   path('api/job_detail_api/<int:id>',api.api_job_detail,name='job_detail'),
]
