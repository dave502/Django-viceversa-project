
#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['textarea1']
	reversed_text = user_text[::-1]
	words_count = len(user_text.split())
	words_count_txt = str(words_count) + (" word" if words_count == 1 else " words")
	print("words_count = " + words_count_txt)  
	return render(request, 'reverse.html', {'user_text':user_text, 
		'reversed_text':reversed_text, 'words_count_txt':words_count_txt})