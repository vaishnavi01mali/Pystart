from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data={
        'title':'Home New',
        'bdata':'Welcome to django project.',
        'clist':['PHP','Java','Django'],
        'numbers':[10,20,30,40,50],
        'student_details':[
           {'name':'pradeep','phone':9269698122},
           {'name':'pradeep','phone':9269698122}
        ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to PyStart")

def course(request):
    return HttpResponse("Welcome")

def courseDetails(request,courseid):
    return HttpResponse(courseid)