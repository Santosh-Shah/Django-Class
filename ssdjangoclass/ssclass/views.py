from django.shortcuts import render

# Create your views here.
def all_ssclass(request):
  return render(request, 'ssclass/all_ssclass.html')