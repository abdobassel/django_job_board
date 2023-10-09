from django.shortcuts import render,Http404,HttpResponse,get_object_or_404
from .models import *
from django.core.paginator import Paginator,Page,PageNotAnInteger

def job_list(request):
    job_list =Job.objects.all()
    

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'jobs':page_obj}


    return render(request, 'job/job_list.html',context)




def job_detail(request,slug,id):
    job_detail = get_object_or_404( Job,slug=slug ,id=id)
    context = {'job':job_detail}
    return render(request, 'job/job_detail.html',context)