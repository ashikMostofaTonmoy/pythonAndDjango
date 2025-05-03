from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World! This is our Django application deployed with CI/CD!") 