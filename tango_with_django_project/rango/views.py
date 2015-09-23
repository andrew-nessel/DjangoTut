from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World <a href='/rango/about/'>go to about<a>")

def about(request):
	return HttpResponse("about")


