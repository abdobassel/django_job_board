from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Job


@api_view(['GET'])
def api_job_list(request):
    all_jobs = Job.objects.all()
    data = JobSerializer(all_jobs,many=True).data
    return Response({'data':data})


@api_view(['GET'])
def api_job_detail(request,id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializer(job_detail).data
    return Response({'data':data})