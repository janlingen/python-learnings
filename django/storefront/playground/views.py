from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello1(request):
    # Pull data from db
    # Transform data
    # Send emails
    return HttpResponse('Hello World')


# respond with an hmtl template
def say_hello2(request):
    return render(request, "hello1.html")


# respond with a dynamic build html template
def say_hello3(request):
    return render(request, "hello2.html", {'name': 'Jan'})


# respond with a dynamic build html template with if statement
def say_hello4(request):
    query = request.GET.get('name')
    return render(request, "hello3.html", {'name': query})


def put_name(request):
    return render(request, "put_name.html")
