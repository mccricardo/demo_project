from django.shortcuts import HttpResponse

def index(request):
	return HttpResponse("Demo App Hello World.")
