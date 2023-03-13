from django.shortcuts import render

# Create your views here.
def jinja1(request):
    D={'name':'Vijji','Age':23}
    return render(request,'jinja1.html',context=D)