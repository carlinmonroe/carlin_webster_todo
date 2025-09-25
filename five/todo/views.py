from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>To-Do</h1><p>It works!</p>")
