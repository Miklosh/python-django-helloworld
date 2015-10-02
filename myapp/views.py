from django.shortcuts import render_to_response

def index1(request):
	return render_to_response('index.html', {'text_test' : 'Hello World', 
		't2': 'Bye World'})

def index2(request):
	return render_to_response('index.html', {'text_test' : 'Yolo!', 
		't2': 'Bye World'})

