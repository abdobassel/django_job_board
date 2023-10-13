from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics 
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

## using generic views api
class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'