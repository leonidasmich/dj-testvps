from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Hello World, I'm Online!")