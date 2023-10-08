from django.shortcuts import render,Http404,HttpResponse,get_object_or_404
from .models import *

def job_list(request):
    job_list =Job.objects.all()
    context = {'jobs':job_list}


    return render(request, 'job/job_list.html',context)




def job_detail(request,id):
    job_detail = get_object_or_404( Job,id=id)
    context = {'job':job_detail}
    return render(request, 'job/job_detail.html',context)